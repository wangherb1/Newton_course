import { Fragment } from 'react';
import { assetPath } from '../data/routes';

type TeacherTextBlockProps = {
  paragraphs: string[];
  figure?: {
    src: string;
    alt: string;
    insertAfterParagraph: number;
  };
};

export default function TeacherTextBlock({ paragraphs, figure }: TeacherTextBlockProps) {
  return (
    <section className="section-card teacher-block">
      <div className="section-heading">
        <p className="section-kicker">Chinese translation</p>
        <h2>中译版</h2>
      </div>
      {paragraphs.map((paragraph, index) => (
        <Fragment key={`${index}-${paragraph.slice(0, 12)}`}>
          <p className={index === 0 ? 'teacher-proposition-statement' : undefined}>
            {index === 0 ? <strong><em>{paragraph}</em></strong> : paragraph}
          </p>
          {figure?.insertAfterParagraph === index && (
            <figure className="teacher-source-figure">
              <img src={assetPath(figure.src)} alt={figure.alt} />
            </figure>
          )}
        </Fragment>
      ))}
    </section>
  );
}
