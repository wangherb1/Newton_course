import theme from '../../../assets/theme/theme.json';

export const siteTheme = theme;

export const siteThemeVariables = [
  `--deep-blue: ${theme.colors.deepBlue}`,
  `--gold: ${theme.colors.gold}`,
  `--parchment: ${theme.colors.parchment}`,
  `--ink-green: ${theme.colors.inkGreen}`,
  `--paper: ${theme.colors.paper}`,
  `--text: ${theme.colors.text}`,
  `--font-cn: ${theme.fonts.chinese}`,
  `--font-en: ${theme.fonts.english}`,
  `--font-math: ${theme.fonts.math}`,
  `--card-radius: ${theme.components.cardRadius}`,
  `--button-radius: ${theme.components.buttonRadius}`,
].join('; ');
