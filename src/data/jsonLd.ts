import { SITE, absoluteUrl } from './site';

const orgId = `${SITE.url}/#organization`;
const websiteId = `${SITE.url}/#website`;

export function organizationSchema() {
  return {
    '@type': 'Organization',
    '@id': orgId,
    name: SITE.name,
    url: SITE.url,
    logo: absoluteUrl('/images/isotipo.png'),
    email: SITE.supportEmail
  };
}

export function websiteSchema() {
  return {
    '@type': 'WebSite',
    '@id': websiteId,
    url: SITE.url,
    name: SITE.name,
    description: SITE.defaultDescription,
    inLanguage: 'en',
    publisher: { '@id': orgId }
  };
}

export function softwareApplicationSchema() {
  return {
    '@type': 'SoftwareApplication',
    name: SITE.name,
    applicationCategory: 'SportsApplication',
    operatingSystem: 'iOS, watchOS',
    description: SITE.defaultDescription,
    url: SITE.url,
    image: absoluteUrl(SITE.ogImage),
    offers: {
      '@type': 'Offer',
      price: '0',
      priceCurrency: 'USD'
    },
    author: { '@id': orgId }
  };
}

export function homePageSchema() {
  return {
    '@context': 'https://schema.org',
    '@graph': [organizationSchema(), websiteSchema(), softwareApplicationSchema()]
  };
}

export function webPageSchema(title: string, description: string, pathname: string) {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebPage',
    name: title,
    description,
    url: absoluteUrl(pathname),
    isPartOf: { '@id': websiteId },
    publisher: { '@id': orgId },
    inLanguage: 'en'
  };
}

export function breadcrumbSchema(items: Array<{ name: string; path: string }>) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, index) => ({
      '@type': 'ListItem',
      position: index + 1,
      name: item.name,
      item: absoluteUrl(item.path)
    }))
  };
}

export function faqSchema(faqs: Array<{ question: string; answer: string }>) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map((faq) => ({
      '@type': 'Question',
      name: faq.question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: faq.answer
      }
    }))
  };
}
