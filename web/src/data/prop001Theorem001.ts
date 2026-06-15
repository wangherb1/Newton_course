export const nodeMeta = {
  id: 'principia-book1-chapter02-prop001-theorem001',
  chapterTitle: '第二章 向心力的确定',
  displayId: '命题1 定理1',
  shortTitle: '扫面积速度恒定',
  titleCn: '仅受向心力作用的物体与固定力心的连线扫面积速度恒定',
  titleEn:
    'The areas described by radii drawn to an immovable centre of force are proportional to the times',
  bookLocation: 'Book I, Section II, Proposition I, Theorem I',
  themeKey: 'chapter02_centripetal_force',
  symbol: '力心 / 面积速度 / 轨道',
};

export const reviewPanel = {
  visible: true,
  items: [
    ['所属章节', nodeMeta.chapterTitle],
    ['节点类型', '命题 / 定理'],
    ['原书位置', nodeMeta.bookLocation],
    ['内容状态', '主体四模块样板范式已基本敲定；扩展模块保留待审阅'],
    ['英文原文状态', '已从 Wikisource 1846 数字页面提取，译文归属 Motte 1729，待人工校对'],
    ['中文译文状态', '已从老师第2章稿件提取，待校对'],
    ['现代解释状态', '已从老师第2章稿件提取，Word 内嵌公式与图2.1已回填，待校对'],
    ['动态演示状态', '已接入独立 HTML 等面积演示文件，按相等时间扫过相等面积建模，待人工审阅'],
    ['思考题状态', '保留当前内容，待后续审阅'],
  ],
} as const;

export const chapterIntro = {
  visible: true,
  source: 'teacher_manuscript',
  paragraphs: [
    '根据物体的运动确定物体的受力，或者反过来，根据物体的受力推测确定物体的运动，这就是今天我们熟悉的运动学和动力学的核心内容。在本章中，牛顿首先给出了作环绕运动的物体，如果只受到指向一个不动点的力（向心力）的作用时，物体的运动应该具有的规律，',
    '在这里分析的环绕运动，都是满足开普勒面积定律的运动，即运动物体与固定中心的连线扫面积速度是恒定的',
  ],
} as const;

export const englishStatement =
  'The areas, which revolving bodies describe by radii drawn to an immovable centre of force do lie in the same immovable planes, and are proportional to the times in which they are described.';

export const englishProof = [
  'For suppose the time to be divided into equal parts, and in the first part of that time let the body by its innate force describe the right line AB. In the second part of that time, the same would (by Law I.), if not hindered, proceed directly to c, along the line Bc equal to AB; so that by the radii AS, BS, cS, drawn to the centre, the equal areas ASB, BSc, would be described.',
  'But when the body is arrived at B, suppose that a centripetal force acts at once with a great impulse; and, turning aside the body from the right line Bc, compels it afterwards to continue its motion along the right line BC. Draw cC parallel to BS meeting BC in C; and at the end of the second part of the time, the body (by Cor. I. of the Laws) will be found in C, in the same plane with the triangle ASB.',
  'Join SC, and, because SB and Cc are parallel, the triangle SBC will be equal to the triangle SBc, and therefore also to the triangle SAB. By the like argument, if the centripetal force acts successively in C, D, E. &c.; and makes the body, in each single particle of time, to describe the right lines CD, DE, EF, &c., they will all lie in the same plane; and the triangle SCD will be equal to the triangle SBC, and SDE to SCD, and SEF to SDE.',
  'And therefore, in equal times, equal areas are described in one immovable plane: and, by composition, any sums SADS, SAFS, of those areas, are one to the other as the times in which they are described. Now let the number of those triangles be augmented, and their breadth diminished in infinitum; and (by Cor. 4, Lem. III.) their ultimate perimeter ADF will be a curve line: and therefore the centripetal force, by which the body is perpetually drawn back from the tangent of this curve, will act continually; and any described areas SADS, SAFS, which are always proportional to the times of description, will, in this case also, be proportional to those times. Q.E.D.',
] as const;

export const teacherProof = [
  '作环绕运动的物体，如果仅受到指向一个不动点的力（向心力）的作用，则物体与不动点的连线始终位于同一平面内，且连线扫过的面积与所用时间成正比。',
  '证明：',
  '设想将时间分为相等的时间段，在第一个时间段里物体在其惯性力作用下沿直线AB运动。如果没有受到妨碍，在第二个时间段里，(由定律I)物体将继续沿直线Bc运动到c，且Bc等于AB；由物体向中心作半径AS，BS，cS，则半径扫过面积ASB，BSc相等。',
  '但是，假设当物体到达B时，一个向心力即刻施以大的冲击作用，迫使其偏离直线Bc，转而沿直线BC运动。作cC平行于BS，与BC相交于C，则在第二个时间段末尾，(由定律推论I)物体将出现在C，与三角形ASB处于同一平面。连接SC，由于SB与Cc平行，三角形SBC与三角形SBc面积相等，因此也与三角形SAB面积相等。',
  '根据同样的理由，如果向心力依次作用于C，D，E等点，将使物体在每一个时间段内经过直线CD，DE，EF等，它们都处于同一平面。而且三角形SCD的面积等于三角形SBC的面积，SDE的面积等于SCD的面积，SEF的面积等于SDE的面积。所以，在相同时间段内，在不动平面上扫过的面积总相等；而且，通过叠加，这些面积的任意和SADS，SAFS都分别正比于扫出它们的时间。',
  '现在，令这些三角形的数目增加，使其底边长无限减小，(由引理3推论4)它们的最终轮廓ADF将成为一条曲线：即向心力连续牵引物体偏离该曲线的切线；任意面积SADS，SAFS总是正比于扫出它们所用的（有限）时间的，在此极限情形下，这些面积仍与所用时间成正比。',
  '证毕。',
];

export const modernExplanation = [
  { type: 'paragraph', segments: ['证明：'] },
  {
    type: 'paragraph',
    segments: [
      '如图2.1所示，假设物体',
      { math: 'm' },
      '初速度为',
      { math: 'v' },
      '，仅受到指向点',
      { math: 'O' },
      '的力',
      { math: 'F' },
      '，',
      { math: 'v' },
      '和',
      { math: 'F' },
      '不在同一方向上，否则物体将做沿该方向的直线运动。物体沿',
      { math: 'v' },
      '和',
      { math: 'F' },
      '所张成平面的法线方向的速度为零（已知）加速度为零（根据牛顿第二定律），因此物体将一直在该平面内运动。',
    ],
  },
  {
    type: 'paragraph',
    segments: [
      '选择点',
      { math: 'O' },
      '为坐标原点，在',
      { math: 'v' },
      '和',
      { math: 'F' },
      '所在平面建立坐标系',
      { math: 'Oxy' },
      '和极坐标系',
      { math: 'Or\\theta' },
      '。',
    ],
  },
  {
    type: 'paragraph',
    segments: [
      '假设时刻',
      { math: 't' },
      '物体处于位置',
      { math: 'P' },
      '，坐标为',
      { math: 'r(t)' },
      '，',
      { math: '\\theta(t)' },
      '，时刻',
      { math: 't + \\Delta t' },
      '物体处于位置',
      { math: 'Q' },
      '，坐标为',
      { math: 'r(t + \\Delta t)' },
      '，',
      { math: '\\theta(t + \\Delta t)' },
      '。',
    ],
  },
  {
    type: 'paragraph',
    segments: [
      '根据引理8，图2.1中曲边三角形',
      { math: '\\overset{\\frown}{OPQ}' },
      '与直边三角形',
      { math: 'OPQ' },
      '的面积在',
      { math: '\\Delta t \\to 0' },
      '时趋于相等，即',
    ],
  },
  {
    type: 'formula',
    formula:
      '\\lim_{\\Delta t \\to 0} S_{\\triangle OPQ} = \\lim_{\\Delta t \\to 0} S_{\\overset{\\frown}{OPQ}}',
  },
  { type: 'paragraph', segments: ['因此有'] },
  {
    type: 'formula',
    formula:
      '\\lim_{\\Delta t \\to 0} \\frac{S_{\\overset{\\frown}{OPQ}}}{\\Delta t} = \\lim_{\\Delta t \\to 0} \\frac{S_{\\triangle OPQ}}{\\Delta t}',
    label: '2.1',
  },
  { type: 'paragraph', segments: ['又注意到'] },
  {
    type: 'formula',
    formula:
      '\\dot S = \\lim_{\\Delta t \\to 0} \\frac{S_{\\triangle OPQ}}{\\Delta t} = \\lim_{\\Delta t \\to 0} \\frac{\\frac{1}{2} r(t) r(t + \\Delta t) \\sin\\!\\left(\\theta(t + \\Delta t) - \\theta(t)\\right)}{\\Delta t} = \\frac{1}{2} r^2(t) \\dot{\\theta}(t)',
    label: '2.2',
  },
  {
    type: 'paragraph',
    segments: ['根据给定条件，物体仅受径向力，在极坐标系中，径向加速度和周向加速度分量分别为'],
  },
  {
    type: 'formula',
    formula: 'a_r = \\ddot r - r\\dot{\\theta}^2 = \\frac{F}{m}',
    label: '2.3',
  },
  {
    type: 'formula',
    formula: 'a_{\\theta} = 2\\dot r\\dot{\\theta} + r\\ddot{\\theta} = 0',
    label: '2.4',
  },
  {
    type: 'paragraph',
    segments: ['由（2.4）对时间', { math: 't' }, '直接积分可知，'],
  },
  {
    type: 'formula',
    formula: 'r^2\\dot{\\theta} = \\operatorname{const}',
    label: '2.5',
  },
  { type: 'paragraph', segments: ['再结合（2.2）可知物体与力心连线扫面积速度'] },
  {
    type: 'formula',
    formula:
      '\\dot S = \\lim_{\\Delta t \\to 0} \\frac{S_{\\triangle OPQ}}{\\Delta t} = \\operatorname{const}',
    label: '2.6',
  },
  { type: 'paragraph', segments: ['因此原命题（定理）成立。'] },
] as const;

export const questions = [
  '本命题要解决的核心问题是什么？',
  '牛顿为什么要先把连续向心力离散成一系列瞬时冲击？',
  '为什么三角形 ASB 与 BSc 面积相等？',
  '当时间段无限缩小时，折线轨迹为什么可以过渡为曲线轨迹？',
  '用现代极坐标方法如何证明扫面积速度恒定？',
  '本命题与开普勒第二定律之间是什么关系？',
];

export const graphLinks = {
  dependsOn: [
    '运动第一定律',
    '运动定律推论1：平行四边形法则',
    '第一章引理3推论4：直边图形的极限是曲边图形',
  ],
  usedBy: [
    '命题2 定理2：命题1的逆命题',
    '命题4 定理4：匀速圆周运动向心力',
    '命题6 定理5：任意轨道下向心力表达',
    '开普勒第二定律',
  ],
  related: ['推论1-6：英文原文已定位，待后续分别建页'],
};
