type NodeGraphLinksProps = {
  dependsOn: string[];
  usedBy: string[];
  related: string[];
};

function LinkList({ title, items }: { title: string; items: string[] }) {
  return (
    <article className="graph-list">
      <h3>{title}</h3>
      <ul>
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </article>
  );
}

export default function NodeGraphLinks({
  dependsOn,
  usedBy,
  related,
}: NodeGraphLinksProps) {
  return (
    <section className="section-card">
      <div className="section-heading">
        <p className="section-kicker">Principia graph</p>
        <h2>命题网络</h2>
      </div>
      <div className="graph-grid">
        <LinkList title="前置依赖" items={dependsOn} />
        <LinkList title="后续关联" items={usedBy} />
        <LinkList title="相关节点" items={related} />
      </div>
    </section>
  );
}
