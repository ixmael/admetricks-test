# Frontend (Full Stack Dev Admetricks)
This application use **VueJS 3** (with Typescript) to show the following items:
* A graphical model implemented with SCSS and VanillaJS placed in the default page (http://host/).
* A graph of the value of dollar in chilean pesos in the dashboard page (http://host/dashboard).

## Setup
First, install the dependencies with:
```sh
yarn install
```

### Work with the project

```sh
yarn run dev
```

### Prepare for Production

```sh
yarn run build
```

## Tests

### Run Unit Tests

```sh
npm run test:unit
```

### Run End-to-End Tests with [Cypress](https://www.cypress.io/)

```sh
npm run test:e2e:dev
```

This runs the end-to-end tests against the Vite development server.
It is much faster than the production build.

But it's still recommended to test the production build with `test:e2e` before deploying (e.g. in CI environments):

```sh
npm run build
npm run test:e2e
```
