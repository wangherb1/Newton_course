import HeroVisual from './HeroVisual';

type NodeHeroProps = {
  chapterTitle: string;
  displayId: string;
  shortTitle: string;
  titleCn: string;
  symbol: string;
  heroVisual?: {
    background_image: string;
    alt: string;
  };
};

export default function NodeHero({
  chapterTitle,
  displayId,
  shortTitle,
  titleCn,
  symbol,
  heroVisual,
}: NodeHeroProps) {
  return (
    <header className="node-hero">
      {heroVisual && <HeroVisual config={heroVisual} />}
      <p className="eyebrow">{chapterTitle}</p>
      <p className="node-hero__id">{displayId}</p>
      <h1>{shortTitle}</h1>
      <p className="node-hero__title">{titleCn}</p>
      <p className="node-hero__symbol">{symbol}</p>
    </header>
  );
}
