This project was created using [Microsoft Web Template Studio](https://github.com/Microsoft/WebTemplateStudio).

## Getting Started

The best way to launch the application is using the [Visual Studio Code Tasks](https://code.visualstudio.com/docs/editor/tasks). In the `vscode/tasks.json` file you can find all the tasks configured for this project.

To launch a task click on the menu `Terminal > Run Task` and select the task to launch (or press `Ctrl+Shift+P` and choose the `Tasks:Run Task` command).

To run the project:

1. Install dependencies using `Install dependencies` task.
2. Start development app using `Start App` task.

## File Structure
```
.
├── .vscode/ - Visual Studio Code configuration files
├── backend/ - Backend App
│ ├── scripts/ - scripts to publish
│ ├── constants.py - Defines the constants for the endpoints and port
│ └── server.py - Configures Port and HTTP Server and provides API routes
├── frontend/ - Frontend App
│ ├── e2e/ - end to end tests
│ ├── scripts/ - scripts to publish
│ ├── src/ Angular app folder
│ │ ├── app - Angular main root module
│ │ │ ├── app-shell - Angular main components
│ └─└─└── app.module.ts - Angular root module.
└── README.md
```

### Frontend

The frontend is based on [Angular cli "ng"](https://angular.io/cli).

The most important scripts in the `package.json` are:
  - start: serves the frontend in development on http://localhost:3000/.
  - build: Builds the frontend app. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.
  - publish: Builds the app for production and moves the output to the `publish` folder.
  - test: execute the unit tests via [Karma](https://karma-runner.github.io).
  - e2e: execute the end-to-end tests via [Protractor](http://www.protractortest.org/)

To start the frontend application manually:
  1. Open a terminal and navigate to the `frontend` folder path.
  2. Use `yarn install` or `npm install` to install frontend dependencies.
  3. Use `yarn start` or `npm start` to start frontend app in development.

### Backend

The backend is based on [Flask](https://github.com/pallets/flask).

To start the backend application manually:
  1. Open a terminal and navigate to the `backend` folder path.
  2. Use `pip install -r requirements.txt` to install backend dependencies.
  3. Use `python3 server/server.py || python server/server.py || py -3 server/server.py` to start backend app in development. It is served on http://localhost:3001/

## Deployment

To deploy the application in an Azure App Service follow the deployment instructions:

- [Deployment using Web Template Studio Deploy command](https://github.com/microsoft/WebTemplateStudio/blob/dev/docs/generated-apps/deployment.md)

Consider adding authentication and securing backend API's by following [Azure App Service Security](https://docs.microsoft.com/en-us/azure/app-service/overview-security).

## Additional Documentation

- Angular Docs - https://angular.io/docs
- Angular Router - https://angular.io/guide/router
- Flask - http://flask.pocoo.org/
- Bootstrap CSS - https://getbootstrap.com/
