const demoSrc = '/demos/book1_chapter02/prop001_theorem001/equal_area_demo.html';

export default function AreaLawDemo() {
  return (
    <figure className="area-law-demo-frame">
      <iframe
        className="area-law-demo-frame__iframe"
        loading="lazy"
        src={demoSrc}
        title="椭圆轨道中的等面积定律动态演示"
      />
      <figcaption className="area-law-demo-frame__caption">
        椭圆轨道以焦点 S 为固定力心。相等时间间隔内，短连线对应较大的转角，长连线对应较小的转角，而焦点连线扫过的面积保持相等。
      </figcaption>
    </figure>
  );
}
