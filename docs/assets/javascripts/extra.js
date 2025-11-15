// AILIS Custom JavaScript
// Enhancements for the documentation site

document.addEventListener('DOMContentLoaded', function() {
  // Add exploratory notice to proposal pages
  safeExecute(addExploratoryNotice);

  // Enhance layer references
  safeExecute(enhanceLayerReferences);

  // Add copy buttons to code blocks (if not already present)
  safeExecute(enhanceCodeBlocks);

  // Add status badges to proposals
  safeExecute(addStatusBadges);

  // Track outbound links
  safeExecute(trackOutboundLinks);

  // Improve accessibility
  safeExecute(improveAccessibility);
});

/**
 * Check if running in development mode
 */
function isDevelopmentMode() {
  return window.location.hostname === 'localhost' ||
         window.location.hostname === '127.0.0.1' ||
         window.location.hostname === '' ||
         window.location.port !== '';
}

/**
 * Safely execute a function with error handling
 */
function safeExecute(fn) {
  try {
    fn();
  } catch (error) {
    // Log errors in development mode for debugging
    if (isDevelopmentMode()) {
      console.error('AILIS Enhancement Error:', error);
      console.error('Function:', fn.name || 'anonymous');
      console.trace();
    }
    // Silently fail in production to prevent page crashes
    // Error doesn't interrupt other enhancements
  }
}

/**
 * Get base path for the site
 */
function getBasePath() {
  // Extract base path from current location
  const path = window.location.pathname;
  const parts = path.split('/').filter(p => p);

  // If in subdirectory (GitHub Pages style), return base
  if (parts.length > 0 && parts[0] === 'AILIS') {
    return '/AILIS';
  }
  return '';
}

/**
 * Add exploratory notice to proposal pages
 */
function addExploratoryNotice() {
  const isProposalPage = window.location.pathname.includes('/proposals/');
  const content = document.querySelector('.md-content article');

  if (isProposalPage && content && !document.querySelector('.exploratory-notice')) {
    const notice = document.createElement('div');
    notice.className = 'exploratory-notice';

    const basePath = getBasePath();
    notice.innerHTML = `
      <h3>🌱 Exploratory Proposal</h3>
      <p>
        This is a proposal for discussion, not a prescriptive standard.
        We welcome critical feedback, alternative approaches, and questions.
        <a href="${basePath}/FEEDBACK">Share your thoughts</a>.
      </p>
    `;

    // Insert after the first heading
    const firstHeading = content.querySelector('h1');
    if (firstHeading && firstHeading.nextElementSibling) {
      firstHeading.parentNode.insertBefore(notice, firstHeading.nextElementSibling);
    }
  }
}

/**
 * Enhance layer references in text
 */
function enhanceLayerReferences() {
  const content = document.querySelector('.md-content article');
  if (!content) return;

  // Find all text nodes
  const walker = document.createTreeWalker(
    content,
    NodeFilter.SHOW_TEXT,
    null,
    false
  );

  const textNodes = [];

  while (walker.nextNode()) {
    if (walker.currentNode.parentElement.tagName !== 'CODE' &&
        walker.currentNode.parentElement.tagName !== 'PRE') {
      textNodes.push(walker.currentNode);
    }
  }

  textNodes.forEach(node => {
    const text = node.textContent;
    // Create new regex instance for each use to avoid state retention
    const layerPattern = /Layer\s+(\d+|[IVX]+):/gi;

    if (layerPattern.test(text)) {
      const span = document.createElement('span');
      // Reset regex and apply replacement
      const replacementPattern = /Layer\s+(\d+|[IVX]+):/gi;
      span.innerHTML = text.replace(replacementPattern, '<span class="layer-reference">Layer $1</span>:');
      node.parentNode.replaceChild(span, node);
    }
  });
}

/**
 * Enhance code blocks with additional features
 */
function enhanceCodeBlocks() {
  const codeBlocks = document.querySelectorAll('pre code');

  codeBlocks.forEach(block => {
    // Add language label if available
    const language = block.className.match(/language-(\w+)/);
    if (language && !block.previousElementSibling?.classList.contains('code-label')) {
      const label = document.createElement('div');
      label.className = 'code-label';
      label.textContent = language[1].toUpperCase();
      label.style.cssText = `
        background: var(--ailis-accent);
        color: white;
        padding: 0.25rem 0.75rem;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        border-radius: 4px 4px 0 0;
        margin-top: 1rem;
      `;
      block.parentElement.parentElement.insertBefore(label, block.parentElement);
    }
  });
}

/**
 * Add status badges to proposal titles
 */
function addStatusBadges() {
  const title = document.querySelector('.md-content h1');
  if (!title) return;

  // Check for status in page metadata or infer from path
  const isDraft = window.location.pathname.includes('draft');
  const isReview = document.querySelector('meta[name="status"]')?.content === 'review';
  const isFinal = document.querySelector('meta[name="status"]')?.content === 'final';

  let status = '';
  let statusClass = '';

  if (isDraft) {
    status = 'Draft';
    statusClass = 'status-draft';
  } else if (isReview) {
    status = 'In Review';
    statusClass = 'status-review';
  } else if (isFinal) {
    status = 'Final';
    statusClass = 'status-final';
  }

  if (status && !title.querySelector('.status-badge')) {
    const badge = document.createElement('span');
    badge.className = `status-badge ${statusClass}`;
    badge.textContent = status;
    badge.style.marginLeft = '1rem';
    title.appendChild(badge);
  }
}

/**
 * Track outbound links for analytics
 */
function trackOutboundLinks() {
  const links = document.querySelectorAll('a[href^="http"]');

  links.forEach(link => {
    if (!link.hostname.includes('dollhousemcp.github.io')) {
      link.addEventListener('click', function(e) {
        // Analytics tracking would go here
        // Removed console.log for privacy
      });

      // Add external link indicator
      if (!link.querySelector('.external-link-icon')) {
        const icon = document.createElement('span');
        icon.className = 'external-link-icon';
        icon.innerHTML = ' ↗';
        icon.style.opacity = '0.6';
        link.appendChild(icon);
      }
    }
  });
}

/**
 * Improve accessibility features
 */
function improveAccessibility() {
  // Add skip to content link if not present
  if (!document.querySelector('.skip-to-content')) {
    const skip = document.createElement('a');
    skip.href = '#main-content';
    skip.className = 'skip-to-content';
    skip.textContent = 'Skip to main content';
    document.body.insertBefore(skip, document.body.firstChild);
  }

  // Add main landmark if not present
  const content = document.querySelector('.md-content');
  if (content && !content.id) {
    content.id = 'main-content';
    content.setAttribute('role', 'main');
  }

  // Enhance keyboard navigation
  const navLinks = document.querySelectorAll('.md-nav__link');
  navLinks.forEach(link => {
    link.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        link.click();
      }
    });
  });

  // Add ARIA labels to icon-only buttons
  const iconButtons = document.querySelectorAll('button:not([aria-label])');
  iconButtons.forEach(button => {
    const icon = button.querySelector('.md-icon');
    if (icon && !button.textContent.trim()) {
      const title = button.getAttribute('title') || 'Button';
      button.setAttribute('aria-label', title);
    }
  });
}

/**
 * Add discussion prompts to specific sections
 */
function highlightDiscussionPrompts() {
  const content = document.querySelector('.md-content article');
  if (!content) return;

  // Find paragraphs that are questions (end with ?)
  const paragraphs = content.querySelectorAll('p');

  paragraphs.forEach(p => {
    const text = p.textContent.trim();
    if (text.endsWith('?') && text.split(' ').length > 5) {
      // Likely a discussion question
      if (!p.classList.contains('discussion-prompt')) {
        p.classList.add('discussion-prompt');
      }
    }
  });
}

/**
 * Smooth scroll for anchor links
 */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });

      // Update URL without jumping
      if (history.pushState) {
        history.pushState(null, null, this.getAttribute('href'));
      }
    }
  });
});

/**
 * Add reading time estimate
 */
function addReadingTime() {
  const content = document.querySelector('.md-content article');
  const title = document.querySelector('.md-content h1');

  if (content && title && !document.querySelector('.reading-time')) {
    const text = content.textContent;
    const wordCount = text.trim().split(/\s+/).length;
    const readingTime = Math.ceil(wordCount / 200); // Assume 200 words per minute

    const timeElement = document.createElement('div');
    timeElement.className = 'reading-time';
    timeElement.textContent = `📖 ${readingTime} min read`;
    timeElement.style.cssText = `
      color: #666;
      font-size: 0.9rem;
      font-style: italic;
      margin-top: 0.5rem;
    `;

    title.parentNode.insertBefore(timeElement, title.nextSibling);
  }
}

// Initialize reading time with error handling
safeExecute(addReadingTime);

// Re-run enhancements when navigation occurs (for SPA-like behavior)
if (typeof document$ !== 'undefined') {
  document$.subscribe(function() {
    safeExecute(addExploratoryNotice);
    safeExecute(enhanceLayerReferences);
    safeExecute(enhanceCodeBlocks);
    safeExecute(addStatusBadges);
    safeExecute(addReadingTime);
  });
}
