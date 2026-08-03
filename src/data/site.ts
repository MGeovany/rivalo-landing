export const SITE = {
  name: 'Rivalo',
  url: 'https://rivalo.thefndrs.com',
  locale: 'en_US',
  defaultTitle: 'Rivalo | Football performance tracking for Apple Watch & iPhone',
  defaultDescription:
    'Track amateur football matches on Apple Watch. Capture distance, sprints, heart rate, and intensity, then review stats, heatmaps, and progress on iPhone.',
  ogImage: '/favicon.png',
  supportEmail: 'marlon.castro@thefndrs.com'
} as const;

export function absoluteUrl(path: string, site = SITE.url): string {
  return new URL(path, site).href;
}
