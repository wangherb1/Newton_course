type QuestionBlockProps = {
  questions: string[];
};

export default function QuestionBlock({ questions }: QuestionBlockProps) {
  return (
    <section className="section-card">
      <div className="section-heading">
        <p className="section-kicker">Study prompts</p>
        <h2>思考题</h2>
      </div>
      <p className="source-note">
        助教整理版：依据《思考题》第2章方向与本命题证明结构拆分，待课程组审阅。
      </p>
      <ol className="question-list">
        {questions.map((question) => (
          <li key={question}>{question}</li>
        ))}
      </ol>
    </section>
  );
}
