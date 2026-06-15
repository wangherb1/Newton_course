type NodeMetaPanelProps = {
  items: ReadonlyArray<readonly [string, string]>;
};

export default function NodeMetaPanel({ items }: NodeMetaPanelProps) {
  return (
    <section className="section-card meta-panel" aria-labelledby="node-meta-title">
      <div className="section-heading">
        <p className="section-kicker">Internal review panel</p>
        <h2 id="node-meta-title">审阅状态</h2>
      </div>
      <p className="meta-panel__notice">
        本模块仅供内部审阅使用。正式发布时统一隐藏，源文件中的状态记录继续保留。
      </p>
      <dl className="meta-grid">
        {items.map(([label, value]) => (
          <div className="meta-item" key={label}>
            <dt>{label}</dt>
            <dd>{value}</dd>
          </div>
        ))}
      </dl>
    </section>
  );
}
