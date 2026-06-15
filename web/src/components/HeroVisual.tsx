import { assetPath } from '../data/routes';

type HeroVisualConfig = {
  background_image: string;
  alt: string;
};

type HeroVisualProps = {
  config: HeroVisualConfig;
};

export default function HeroVisual({ config }: HeroVisualProps) {
  return (
    <figure className="hero-visual">
      <img alt={config.alt} className="hero-visual__image" src={assetPath(config.background_image)} />
    </figure>
  );
}
