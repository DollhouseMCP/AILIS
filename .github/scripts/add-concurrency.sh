#!/bin/bash
# Script to add concurrency configuration to workflow files

WORKFLOW_DIR=".github/workflows"

# Array of workflow files and their concurrency group names
declare -A workflows=(
    ["markdown-lint.yml"]="markdown-lint"
    ["spell-check.yml"]="spell-check" 
    ["accessibility-check.yml"]="accessibility-check"
    ["proposal-lifecycle.yml"]="proposal-lifecycle"
    ["proposal-stage-transitions.yml"]="stage-transitions"
    ["discussion-notifications.yml"]="discussion-notifications"
    ["metrics-collection.yml"]="metrics-collection"
)

# Function to add concurrency configuration
add_concurrency() {
    local file="$1"
    local group_name="$2"
    
    echo "Adding concurrency config to $file..."
    
    # Create temporary file with concurrency block
    local temp_file=$(mktemp)
    local added_concurrency=false
    
    while IFS= read -r line; do
        echo "$line" >> "$temp_file"
        
        # Add concurrency block after the 'on:' section
        if [[ "$line" =~ ^[[:space:]]*-[[:space:]]*cron: ]] && [ "$added_concurrency" = false ]; then
            # Find the end of the on: block and add concurrency
            echo "" >> "$temp_file"
            echo "concurrency:" >> "$temp_file"
            echo "  group: ${group_name}-\${{ github.event.pull_request.number || github.ref }}" >> "$temp_file"
            echo "  cancel-in-progress: true" >> "$temp_file"
            added_concurrency=true
        fi
    done < "$WORKFLOW_DIR/$file"
    
    # If no cron job found, add after jobs: line or before jobs:
    if [ "$added_concurrency" = false ]; then
        # Reset temp file and try different approach
        > "$temp_file"
        
        while IFS= read -r line; do
            echo "$line" >> "$temp_file"
            
            # Look for end of on: block (blank line followed by permissions: or jobs:)
            if [[ "$line" =~ ^[[:space:]]*$ ]] && [ "$added_concurrency" = false ]; then
                # Peek at next line
                next_line=$(head -n +$(($(wc -l < "$WORKFLOW_DIR/$file") + 1)) "$WORKFLOW_DIR/$file" | tail -n 1)
                if [[ "$next_line" =~ ^(permissions:|jobs:) ]]; then
                    echo "concurrency:" >> "$temp_file"
                    echo "  group: ${group_name}-\${{ github.event.pull_request.number || github.ref }}" >> "$temp_file"
                    echo "  cancel-in-progress: true" >> "$temp_file"
                    echo "" >> "$temp_file"
                    added_concurrency=true
                fi
            fi
        done < "$WORKFLOW_DIR/$file"
    fi
    
    # Move temp file back if concurrency was added
    if [ "$added_concurrency" = true ]; then
        mv "$temp_file" "$WORKFLOW_DIR/$file"
        echo "✅ Added concurrency config to $file"
    else
        rm "$temp_file"
        echo "⚠️  Could not add concurrency config to $file - manual intervention needed"
    fi
}

# Main execution
echo "🔧 Adding concurrency configuration to workflow files..."
echo

for workflow_file in "${!workflows[@]}"; do
    if [ -f "$WORKFLOW_DIR/$workflow_file" ]; then
        add_concurrency "$workflow_file" "${workflows[$workflow_file]}"
    else
        echo "❌ File not found: $WORKFLOW_DIR/$workflow_file"
    fi
    echo
done

echo "✅ Concurrency configuration script completed!"