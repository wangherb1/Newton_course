const baseUrl = import.meta.env.BASE_URL || '/';

export function withBase(path: string) {
  if (!path || path.startsWith('#') || /^[a-z][a-z0-9+.-]*:/i.test(path)) {
    return path;
  }

  const cleanBase = baseUrl.endsWith('/') ? baseUrl.slice(0, -1) : baseUrl;
  const cleanPath = path.startsWith('/') ? path : `/${path}`;

  return cleanBase ? `${cleanBase}${cleanPath}` : cleanPath;
}

export const assetPath = withBase;

export const siteRoutes = {
  home: withBase('/'),
  outline: withBase('/outline/'),
  sampleProp001Theorem001: withBase('/nodes/book1-chapter02/prop001-theorem001/'),
  learningPathsAnchor: '#learning-paths',
} as const;
