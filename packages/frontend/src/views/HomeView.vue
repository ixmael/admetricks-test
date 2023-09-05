<script setup lang="ts">
import { ref, onMounted, } from 'vue';

const content = ref();
const contentA = ref();
const canvas = ref();
const topSquares = ref();

const width = ref(0);
const height = ref(0);

const draw = () => {
  // Get the size of main container
  width.value = content.value.clientWidth;
  height.value = content.value.clientHeight;

  // Set a pixel less for each side
  canvas.value.width = content.value.clientWidth % 2 === 0 ? content.value.clientWidth - 2 : content.value.clientWidth - 3;
  canvas.value.height = content.value.clientHeight;

  // Calculate size of the container
  const a = Math.floor(contentA.value.clientWidth / 4);
  const delay = Math.floor((width.value - contentA.value.clientWidth) / 2);

  const ctx = canvas.value.getContext('2d');

  // Draw all the lines
  drawLine(ctx, delay + 6, 0, delay + 6, height.value - 150, 'rgba(255, 255, 255, 0.1)', 1);
  drawLine(ctx, (a) + delay - 1, 0, (a) + delay - 1, height.value - 150, 'rgba(255, 255, 255, 0.1)', 1);
  drawLine(ctx, (2 * a) + delay, 0, (2 * a) + delay, height.value - 150, 'rgba(255, 255, 255, 0.1)', 1);
  drawLine(ctx, (3 * a) + delay - 18, 0, (3 * a) + delay - 18, height.value - 150, 'rgba(255, 255, 255, 0.1)', 1);
  drawLine(ctx, (4 * a) + delay, 0, (4 * a) + delay - 18, height.value - 150, 'rgba(255, 255, 255, 0.1)', 1);

  // Draw a triangle
  ctx.beginPath();
  ctx.moveTo(content.value.clientWidth - 160, 230);
  ctx.lineTo(content.value.clientWidth - 386, 396);
  ctx.lineTo(content.value.clientWidth + 50, 396);
  ctx.lineTo(content.value.clientWidth - 160, 230);
  ctx.strokeStyle = 'rgba(66, 50, 92, 1)';
  ctx.lineWidth = 1;
  ctx.stroke();
  drawLine(ctx, content.value.clientWidth - 160, 230, content.value.clientWidth - 400, 230, 'rgba(255, 255, 255, 0.1)', 1);
  drawLine(ctx, content.value.clientWidth - 386, 396, content.value.clientWidth - 525, 500, 'rgba(255, 255, 255, 0.1)', 1);

  //
  drawLine(ctx, content.value.clientWidth - 200, 400, content.value.clientWidth + 100, 700, 'rgba(255, 0, 0, 0.3)', 1);
  drawLine(ctx, content.value.clientWidth - 70, 530, content.value.clientWidth + 100, 1200, 'rgba(255, 100, 0, 0.3)', 1);
  drawLine(ctx, content.value.clientWidth - 28, 698, content.value.clientWidth - 120, 1000, 'rgba(255, 255, 0, 0.3)', 1);
  drawLine(ctx, content.value.clientWidth + 30, 900, content.value.clientWidth - 120, 1000, 'rgba(255, 100, 0, 0.3)', 1);
  drawLine(ctx, content.value.clientWidth - 120, 1000, content.value.clientWidth - 300, 1000, 'rgba(22, 53, 60, 1)', 1);
  drawLine(ctx, content.value.clientWidth - 71, 840, content.value.clientWidth - 300, 1000, 'rgba(22, 53, 60, 1)', 1);
  drawLine(ctx, content.value.clientWidth - 500, 800, content.value.clientWidth - 300, 1000, 'rgba(22, 53, 60, 1)', 1);
  drawLine(ctx, content.value.clientWidth - 71, 840, content.value.clientWidth - 200, 840, 'rgba(22, 53, 60, 1)', 1);

  //
  const ts = topSquares.value.getBoundingClientRect();
  const tsx = Math.floor(ts.x);
  const tsy = Math.floor(ts.y);
  ctx.beginPath();
  ctx.moveTo(tsx + 200, tsy - 50);
  ctx.lineTo(tsx + 150, tsy + 100);
  ctx.lineTo(tsx + 250, tsy + 100);
  ctx.lineTo(tsx + 200, tsy - 50);
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
  ctx.lineWidth = 1;
  ctx.stroke();
};

const drawLine = (ctx: any, x1: number, y1: number, x2: number, y2: number, stroke = 'black', width = 3) => {
  // start a new path
  ctx.beginPath();

  // place the cursor from the point the line should be started 
  ctx.moveTo(x1, y1);

  // draw a line from current cursor position to the provided x,y coordinate
  ctx.lineTo(x2, y2);

  // set strokecolor
  ctx.strokeStyle = stroke;

  // set lineWidht 
  ctx.lineWidth = width;

  // add stroke to the line 
  ctx.stroke();
};

onMounted(() => {
  window.addEventListener('resize', draw);
  draw();
});
</script>

<template>
  <main id="content" ref="content">
    <canvas id="extra" ref="canvas" width="1" height="1"></canvas>
    <div class="content" ref="contentA">
      <div class="top">
        <div class="content">
          <div class="a">Estamos para ayudarte</div>
          <h2>
            ¿Tienes problemas para entender el mercado de la publicidad digital?
          </h2>
          <div class="b">
            El Mercado de la publicidad online es incierto y complejo, Admetricks te <span class="remark">ayuda a
              visibilizar cómo desempeñan las campañas y contenidos</span> versus los de tu competencia en tiempo real con
            reportes y alertas automáticas
          </div>
          <div>
            <a class="demo-call" href="#">Solicitar demo</a>
            <a class="functionalities" href="#">Ver funcionalidades</a>
          </div>
          <div class="color-bar"></div>
        </div>
        <div class="topSquares" ref="topSquares">
          <div class="bottom"></div>
          <div class="top"></div>
        </div>
      </div>

      <div class="details">
        <div class="detail">
          <div class="image">
            <img src="/agencias.png" />
          </div>
          <h3>Agencias</h3>
          <p>Crea mejores estrategias de marketing digital, planes de medios y reportes de resultados para tus clientes.
            Muéstrale qué está haciendo su competencia en publicidad online.</p>
        </div>
        <div class="detail">
          <div class="image">
            <img src="/medios.png" />
          </div>
          <h3>Medios</h3>
          <p>Mejora tus argumentos de ventas conociendo en detalle la inversión de tus clientes en otros medios y el
            alcance
            que les aporta.us clientes en otros medios y el alcance que les aporta.</p>
        </div>
        <div class="detail">
          <div class="image">
            <img src="/marcas.png" />
          </div>
          <h3>Marcas</h3>
          <p>Descubre las ofertas y campañas que tu competencia está promocionando. Recibe alertas cuando tu competencia
            lanza una nueva campaña de publicidad online.</p>
        </div>
        <div class="detail">
          <div class="image">
            <img src="/verificacion.png" />
          </div>
          <h3>Verificación</h3>
          <p>Como un agente tercero, transparente y sin conflictos de interés, Admetricks permite a los actores de la
            industria del marketing digital verificar que sus campañas exhiban en los sitios y formatos pautados.</p>
        </div>
      </div>

      <div class="squares">
        <div class="item1"></div>
        <div class="item2"></div>
        <div class="item3"></div>
        <div class="item4"></div>
        <div class="item5"></div>
        <div class="triangles triangle2"></div>
      </div>
    </div>
    <div class="triangles triangle1"></div>
    <div class="triangles triangle3"></div>
  </main>
</template>

<style scoped lang="scss">
main {
  position: relative;
  padding-top: 36rem;
  background-image: url('/background.png');
  background-position-x: 40%;
  background-position-y: 0;
  font-family: 'Poppins', sans-serif;
  padding-bottom: 5vh;
  display: flex;
  justify-content: center;
  overflow: hidden;

  & #extra {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 1;
    bottom: 0;
    right: 0;
  }

  & .content {
    position: relative;
    z-index: 10;
    width: 930px;

    @media (min-width: 1268px) {
      width: 1268;
    }

    @media (max-width: 800px) {
      margin: 0 1rem;
    }

    & .top {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 50vh;
      overflow: hidden;

      & .content {
        color: #fff;
        width: 100%;
        padding: 0 0 0 25px;
        position: relative;

        & .a {
          color: #00d4ff;
          font-weight: bold;
          padding-bottom: 17px;
        }

        & h2 {
          font-size: 1.7rem;
          font-weight: bold;
          line-height: 2.7rem;
          position: relative;
          z-index: 10;
        }

        & .b {
          font-size: 0.9rem;
          margin-top: 45px;
          margin-bottom: 1rem;
          line-height: 1.3rem;
          color: rgba(255, 255, 255, 0.7);

          & .remark {
            font-weight: bold;
            color: #00d4ff;
          }
        }

        & .demo-call {
          color: #000;
          background-color: #00d4ff;
          padding: 10px 30px 10px 30px;
          border-radius: 20px;
          text-decoration: none;
          font-weight: bold;
          display: inline-block;
          margin-right: 15px;
          font-size: 0.8125rem;
        }

        & .color-bar {
          background: rgb(0, 119, 160);
          background: linear-gradient(90deg, rgba(0, 119, 160, 1) 0%, rgba(67, 112, 0, 1) 100%);
          position: absolute;
          width: 250px;
          height: 15px;
          left: 130px;
          top: 100px;
          border-radius: 10px;
          z-index: 1;
        }

        & .functionalities {
          color: #fff;
          text-decoration: none;
          font-weight: bold;
          display: inline-block;
          font-size: 0.8125rem;
        }
      }

      & .topSquares {
        position: relative;
        height: 100%;
        width: 100%;

        &>div {
          border-radius: 30px;
          border-color: #fff;
          border-style: solid;
          border-width: 1px;
          background-color: #18324d;
        }

        & .bottom {
          position: absolute;
          left: 10%;
          top: 10%;
          height: 80%;
          width: 70%;
          z-index: 10;
        }

        & .top {
          position: absolute;
          right: 0;
          top: 0;
          z-index: 20;
          width: 40%;
          height: 99%;
        }
      }
    }

    .details {
      display: flex;
      justify-content: space-evenly;
      align-items: flex-start;
      margin-top: 45px;
      margin-bottom: 150px;

      & .detail {
        margin: 0 5px;

        & .image {
          height: 33px;
          margin-bottom: 10px;
          padding-left: 17px;
        }

        & h3 {
          color: #fff;
          font-weight: bold;
          border-left-style: solid;
          border-left-color: #00d4ff;
          border-left-width: 2px;
          padding: 0 0 5px 17px;
          margin-bottom: 10px;
        }

        & p {
          color: #fff;
          font-size: 0.8rem;
          padding-left: 17px;
          padding-right: 40px;
        }
      }
    }

    .squares {
      display: block;
      position: relative;
      height: 900px;
      padding-bottom: 150px;

      & div {
        position: absolute;
        padding: 0;
        margin: 0;

        &[class^='item'] {
          background-color: #fff;
          border-radius: 30px;
        }

        &.item1 {
          width: 30%;
          height: 20%;
          top: 5%;
          left: 1%;
        }

        &.item2 {
          width: 50%;
          height: 40%;
          left: 33%;
          top: 5%;
        }

        &.item3 {
          width: 15%;
          height: 45%;
          right: 0;
          top: 0;
        }

        &.item4 {
          width: 30%;
          height: 60%;
          left: 0;
          top: 27%;
        }

        &.item5 {
          width: 66%;
          height: 44%;
          right: 4px;
          top: 500px;
        }
      }
    }

    // Squares
  }

  // Content
  .triangles {
    position: absolute;
    z-index: 100;
  }

  .triangle1 {
    background-image: url('/green.png');
    background-repeat: no-repeat;
    background-position: center;
    left: -90px;
    top: 86px;
    width: 250px;
    height: 253px;
  }

  .triangle2 {
    background-image: url('/yellow.png');
    background-repeat: no-repeat;
    background-position: center;
    left: -70px;
    top: -40px;
    width: 207px;
    height: 202px;
  }

  & .triangle3 {
    background-image: url('/orange.png');
    background-repeat: no-repeat;
    background-position: center;
    left: -101px;
    bottom: -85px;
    width: 359px;
    height: 366px;
  }
}
</style>
