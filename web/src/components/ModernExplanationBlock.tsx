import katex from 'katex';
import 'katex/dist/katex.min.css';
import { assetPath } from '../data/routes';

type InlineSegment = string | { math: string };

type ModernExplanationItem =
  | {
      type: 'paragraph';
      segments: readonly InlineSegment[];
    }
  | {
      type: 'formula';
      formula: string;
      label?: string;
    };

type ModernExplanationBlockProps = {
  items: readonly ModernExplanationItem[];
  figure?: {
    src: string;
    alt: string;
    caption?: string;
  };
};

function MathExpression({
  formula,
  displayMode = false,
}: {
  formula: string;
  displayMode?: boolean;
}) {
  return (
    <span
      className={displayMode ? 'modern-formula' : 'modern-inline-formula'}
      dangerouslySetInnerHTML={{
        __html: katex.renderToString(formula, {
          displayMode,
          throwOnError: true,
        }),
      }}
    />
  );
}

export default function ModernExplanationBlock({ items, figure }: ModernExplanationBlockProps) {
  return (
    <section className="section-card modern-block">
      <div className="section-heading">
        <p className="section-kicker">Modern calculus proof in polar coordinates</p>
        <h2>现代微积分证明：极坐标方法</h2>
      </div>
      {figure && (
        <figure className="modern-source-figure">
          <img src={assetPath(figure.src)} alt={figure.alt} />
          {figure.caption && <figcaption>{figure.caption}</figcaption>}
        </figure>
      )}
      {items.map((item, index) => {
        if (item.type === 'formula') {
          return (
            <div className="modern-formula-row" key={`${index}-${item.formula}`}>
              <MathExpression formula={item.formula} displayMode />
              {item.label && <span className="modern-formula-label">（{item.label}）</span>}
            </div>
          );
        }

        return (
          <p key={`${index}-${item.segments[0]}`}>
            {item.segments.map((segment, segmentIndex) =>
              typeof segment === 'string' ? (
                segment
              ) : (
                <MathExpression formula={segment.math} key={`${segmentIndex}-${segment.math}`} />
              ),
            )}
          </p>
        );
      })}
    </section>
  );
}
