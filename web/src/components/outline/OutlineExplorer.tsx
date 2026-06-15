import { useMemo, useState } from 'react';
import {
  statusLabels,
  type PrincipiaNodeStatus,
  type PrincipiaNodeType,
  type PrincipiaOutlineNode,
} from '../../data/principiaOutline';

type Props = {
  groups: PrincipiaOutlineNode[];
};

const typeFilters: Array<[string, string]> = [
  ['all', '全部'],
  ['definition', '定义'],
  ['law', '定律'],
  ['lemma', '引理'],
  ['proposition', '命题'],
  ['corollary', '推论'],
  ['scholium', '附注'],
];

const statusFilters: Array<[string, string]> = [
  ['all', '全部'],
  ['completed_sample', '已完成样板页'],
  ['in_progress', '建设中'],
  ['teacher_text_available', '已有老师稿件'],
  ['outline_only', '仅目录占位'],
  ['needs_review', '待校对'],
];

function matchesType(nodeType: PrincipiaNodeType, filter: string) {
  if (filter === 'all') return true;
  if (filter === 'proposition') return nodeType.startsWith('proposition_') && !nodeType.endsWith('corollary');
  if (filter === 'corollary') return nodeType.endsWith('corollary');
  return nodeType === filter;
}

function ContentFlags({ node }: { node: PrincipiaOutlineNode }) {
  const flags = [
    node.has_english && '英文原文',
    node.has_teacher_translation && '中文译文',
    node.has_modern_explanation && '现代解释',
    node.has_demo && '动态演示',
    node.has_questions && '思考题',
  ].filter(Boolean);

  return <span className="outline-node__flags">{flags.length ? flags.join(' / ') : '目录占位'}</span>;
}

function NodeRow({ node }: { node: PrincipiaOutlineNode }) {
  const body = (
    <>
      <div className="outline-node__main">
        <strong>{node.display_id}</strong>
        <span>{node.title_cn}</span>
      </div>
      <div className="outline-node__meta">
        <span className={`status-badge status-badge--${node.status}`}>
          {statusLabels[node.status as PrincipiaNodeStatus]}
        </span>
        <ContentFlags node={node} />
      </div>
    </>
  );

  return node.route ? (
    <a className="outline-node outline-node--linked" href={node.route}>{body}</a>
  ) : (
    <div className="outline-node outline-node--disabled">{body}</div>
  );
}

export default function OutlineExplorer({ groups }: Props) {
  const [query, setQuery] = useState('');
  const [typeFilter, setTypeFilter] = useState('all');
  const [statusFilter, setStatusFilter] = useState('all');

  const filteredGroups = useMemo(() => {
    const normalized = query.trim().toLocaleLowerCase('zh-CN');
    return groups
      .map((group) => ({
        ...group,
        children: (group.children ?? []).filter((node) => {
          const matchesQuery = !normalized
            || `${node.display_id} ${node.title_cn}`.toLocaleLowerCase('zh-CN').includes(normalized);
          return matchesQuery
            && matchesType(node.node_type, typeFilter)
            && (statusFilter === 'all' || node.status === statusFilter);
        }),
      }))
      .filter((group) => (group.children?.length ?? 0) > 0);
  }, [groups, query, statusFilter, typeFilter]);

  const visibleCount = filteredGroups.reduce((total, group) => total + (group.children?.length ?? 0), 0);

  return (
    <section className="outline-explorer">
      <div className="outline-toolbar">
        <label className="outline-search">
          <span>搜索目录</span>
          <input
            onChange={(event) => setQuery(event.target.value)}
            placeholder="搜索命题1、引理11、向心力、平方反比、正矢..."
            type="search"
            value={query}
          />
        </label>
        <label>
          <span>类型</span>
          <select onChange={(event) => setTypeFilter(event.target.value)} value={typeFilter}>
            {typeFilters.map(([value, label]) => <option key={value} value={value}>{label}</option>)}
          </select>
        </label>
        <label>
          <span>状态</span>
          <select onChange={(event) => setStatusFilter(event.target.value)} value={statusFilter}>
            {statusFilters.map(([value, label]) => <option key={value} value={value}>{label}</option>)}
          </select>
        </label>
      </div>
      <p className="outline-result-count">当前显示 {visibleCount} 个条目</p>
      <div className="outline-groups">
        {filteredGroups.map((group) => (
          <details
            className="outline-group"
            key={`${group.id}-${query}-${typeFilter}-${statusFilter}`}
            open={Boolean(query) || ['front_matter', 'book1_chapter01', 'book1_chapter02'].includes(group.id)}
          >
            <summary>
              <span><strong>{group.display_id}</strong>{group.title_cn}</span>
              <small>{group.children?.length ?? 0} 个条目</small>
            </summary>
            <div className="outline-group__body">
              {group.children?.map((node) => <NodeRow key={node.id} node={node} />)}
            </div>
          </details>
        ))}
      </div>
    </section>
  );
}
