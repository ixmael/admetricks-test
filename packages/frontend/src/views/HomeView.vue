<template>
  <main>
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
      </div>
      <div class="topSquares">
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
        <p>Mejora tus argumentos de ventas conociendo en detalle la inversión de tus clientes en otros medios y el alcance
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
    </div>
  </main>
</template>

<style scoped lang="scss">
main {
  position: relative;
  padding-top: 50vh;

  background-color: #fff;
  background-image: url('/background.png');
  background-position-x: 50%;
  background-position-y: top;
  font-family: 'Poppins', sans-serif;
  padding-bottom: 5vh;
}

.top {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50vh;
  overflow: hidden;

  & .content {
    color: #fff;
    width: 100%;

    & .a {
      color: #00d4ff;
      font-weight: bold;
      padding-bottom: 17px;
    }

    & h2 {
      font-size: 1.7rem;
      font-weight: bold;
    }

    & .b {
      font-size: 1rem;
      margin-top: 45px;
      margin-bottom: 1rem;

      & .remark {
        font-weight: bold;
        color: #00d4ff;
      }
    }

    & .demo-call {
      color: #000;
      background-color: #00d4ff;
      padding: 9px 35px 20px 35px;
      border-radius: 20px;
      text-decoration: none;
      font-weight: bold;
      display: inline-block;
      margin-right: 15px;
      font-size: 0.8125rem;
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
      border-radius: 25px;
      border-color: #fff;
      border-style: solid;
      border-width: 1px;
    }

    & .bottom {


      position: absolute;
      background: transparent;
      left: 150px;
      top: 20px;
      height: 160px;
      width: 200px;
      z-index: 10;
    }

    & .top {
      position: absolute;
      right: 0;
      top: 0;
      z-index: 20;
      background: #18324d;
      width: 150px;
      height: 250px;
    }
  }
}

.details {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  padding: 150px 0;
  height: 30vh;

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
  height: 1100px;

  & div {
    position: absolute;
    background-color: #fff;
    border-radius: 30px;
    padding: 5px;
    width: 200px;
    height: 200px;
    margin: 5px;

    &.item1 {
      width: 300px;
      height: 150px;
      top: 50px;
    }

    &.item2 {
      width: 400px;
      height: 400px;
      right: 200px;
      top: 50px;
    }

    &.item3 {
      width: 150px;
      height: 450px;
      right: 0;
      top: 0;
    }

    &.item4 {
      width: 300px;
      height: 500px;
      left: 0;
      top: 250px;
    }

    &.item5 {
      width: 600px;
      height: 400px;
      right: 0;
      top: 500px;
    }
  }
}
</style>
