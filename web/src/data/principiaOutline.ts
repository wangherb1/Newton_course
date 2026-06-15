import seed from '../../../content/metadata/principia_outline.seed.json';
import { siteRoutes } from './routes';

export type PrincipiaNodeStatus =
  | 'completed_sample'
  | 'in_progress'
  | 'teacher_text_available'
  | 'outline_only'
  | 'pending'
  | 'needs_review';

export type PrincipiaNodeType =
  | 'front_matter'
  | 'definition'
  | 'law'
  | 'law_corollary'
  | 'lemma'
  | 'lemma_corollary'
  | 'proposition_theorem'
  | 'proposition_problem'
  | 'proposition_corollary'
  | 'scholium'
  | 'appendix'
  | 'chapter'
  | 'section';

export type PrincipiaOutlineNode = {
  id: string;
  book?: number;
  part?: string;
  chapter_id?: string;
  chapter_title?: string;
  node_type: PrincipiaNodeType;
  display_id: string;
  title_cn: string;
  short_title?: string;
  route?: string | null;
  status: PrincipiaNodeStatus;
  has_english?: boolean;
  has_teacher_translation?: boolean;
  has_modern_explanation?: boolean;
  has_demo?: boolean;
  has_questions?: boolean;
  sample_page?: boolean;
  source_line?: number;
  children?: PrincipiaOutlineNode[];
};

type SeedItem = {
  source_line: number;
  candidate_type: string;
  text: string;
};

const SAMPLE_NODE_ID = 'principia-book1-chapter02-prop001-theorem001';
const SAMPLE_ROUTE = siteRoutes.sampleProp001Theorem001;

const chineseNumbers: Record<string, number> = {
  一: 1,
  二: 2,
  三: 3,
  四: 4,
  五: 5,
  六: 6,
  七: 7,
  八: 8,
  九: 9,
  十: 10,
  十一: 11,
  十二: 12,
  十三: 13,
  十四: 14,
};

const chapterPattern = /^第(一|二|三|四|五|六|七|八|九|十|十一|十二|十三|十四)章\s*(.*)$/;
const displayPattern =
  /^((?:定义|引理|命题|推论)\s*\d+(?:\s*(?:定理|问题)\s*\d+)?|第[一二三]定律|附注|补充命题\s*补充问题)(?:[：:\s]+)?(.*)$/;

export const statusLabels: Record<PrincipiaNodeStatus, string> = {
  completed_sample: '已完成样板页',
  in_progress: '建设中',
  teacher_text_available: '已有老师稿件',
  outline_only: '目录占位',
  pending: '待建设',
  needs_review: '待校对',
};

function classifyNode(text: string, parentType?: PrincipiaNodeType): PrincipiaNodeType {
  if (/^定义/.test(text)) return 'definition';
  if (/^第[一二三]定律/.test(text)) return 'law';
  if (/^引理/.test(text)) return 'lemma';
  if (/^命题/.test(text) && /问题/.test(text)) return 'proposition_problem';
  if (/^命题/.test(text)) return 'proposition_theorem';
  if (/^推论/.test(text) && parentType === 'law') return 'law_corollary';
  if (/^推论/.test(text) && parentType === 'lemma') return 'lemma_corollary';
  if (/^推论/.test(text)) return 'proposition_corollary';
  if (/^附注/.test(text)) return 'scholium';
  if (/^附录/.test(text)) return 'appendix';
  return 'section';
}

function splitDisplay(text: string) {
  const match = text.match(displayPattern);
  if (!match) return { displayId: text, title: '' };
  return { displayId: match[1].replace(/\s+/g, ' ').trim(), title: match[2].trim() };
}

function getPlaceholderStatus(chapterId?: string): PrincipiaNodeStatus {
  if (!chapterId || ['front_matter', 'book1_chapter01', 'book1_chapter02'].includes(chapterId)) {
    return 'teacher_text_available';
  }
  return 'outline_only';
}

function buildNode(
  item: SeedItem,
  chapter: PrincipiaOutlineNode,
  parentType?: PrincipiaNodeType,
): PrincipiaOutlineNode {
  const isSample = item.text.startsWith('命题1 定理1');
  const { displayId, title } = splitDisplay(item.text);
  const nodeType = classifyNode(item.text, parentType);

  return {
    id: isSample ? SAMPLE_NODE_ID : `principia-${chapter.id}-${String(item.source_line).padStart(3, '0')}`,
    book: chapter.id === 'front_matter' ? undefined : 1,
    part: chapter.id === 'front_matter' ? '卷首' : '第一卷 物体的运动',
    chapter_id: chapter.id,
    chapter_title: chapter.title_cn,
    node_type: nodeType,
    display_id: displayId,
    title_cn: title || item.text,
    short_title: isSample ? '扫面积速度恒定' : undefined,
    route: isSample ? SAMPLE_ROUTE : null,
    status: isSample ? 'completed_sample' : getPlaceholderStatus(chapter.id),
    has_english: isSample,
    has_teacher_translation: isSample,
    has_modern_explanation: isSample,
    has_demo: isSample,
    has_questions: isSample,
    sample_page: isSample,
    source_line: item.source_line,
  };
}

function createChapter(id: string, displayId: string, title: string): PrincipiaOutlineNode {
  return {
    id,
    book: id === 'front_matter' ? undefined : 1,
    part: id === 'front_matter' ? '卷首' : '第一卷 物体的运动',
    node_type: id === 'front_matter' ? 'front_matter' : 'chapter',
    display_id: displayId,
    title_cn: title,
    status: id === 'book1_chapter02' ? 'in_progress' : getPlaceholderStatus(id),
    children: [],
  };
}

function buildOutline(items: SeedItem[]) {
  const groups: PrincipiaOutlineNode[] = [
    createChapter('front_matter', '卷首', '定义、公理与运动定律'),
  ];
  let activeGroup = groups[0];
  let parentType: PrincipiaNodeType | undefined;
  let reachedChapterFourteen = false;

  for (const item of items) {
    if (reachedChapterFourteen && item.text === '定义和定律') break;

    const chapterMatch = item.text.match(chapterPattern);
    if (chapterMatch) {
      const chapterNumber = chineseNumbers[chapterMatch[1]];
      activeGroup = createChapter(
        `book1_chapter${String(chapterNumber).padStart(2, '0')}`,
        `第${chapterMatch[1]}章`,
        chapterMatch[2],
      );
      groups.push(activeGroup);
      parentType = undefined;
      if (chapterNumber === 14) reachedChapterFourteen = true;
      continue;
    }

    const node = buildNode(item, activeGroup, parentType);
    activeGroup.children?.push(node);
    if (!node.node_type.endsWith('corollary')) parentType = node.node_type;
  }

  return groups;
}

export const outlineSource = {
  sourceFile: seed.source_file,
  generatedAt: seed.generated_at,
  paragraphCount: seed.source_paragraph_count,
  candidateCount: seed.candidate_count,
  needsManualReview: seed.needs_manual_review,
};

export const principiaOutline = buildOutline(seed.items as SeedItem[]);
export const flatOutlineNodes = principiaOutline.flatMap((group) => group.children ?? []);
export const chapter02 = principiaOutline.find((group) => group.id === 'book1_chapter02');
export const sampleNode = flatOutlineNodes.find((node) => node.id === SAMPLE_NODE_ID);
