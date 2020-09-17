## Getting Started

1. Install dependencies using `Install dependencies` task (or use `yarn install` or `npm install` frontend folder and `dotnet restore` in backend folder).
2. Start development app using `Start App` task (or use `yarn start` or `npm start` in frontend folder and `dotnet run` in backend folder).

## Next Steps

### Adding a New Page

1. Create a folder in `frontend/src/components` with your react components.
2. Add a route for your page to `frontend/src/App.jsx`.
3. Add a button to the navigation bar in `frontend/src/components/NavBar/index.jsx`.

### Sample Data

Replace the sample data stored in /backend/Services/SampleDataService.cs
Replace the default images. Sample images are consumed from https://wtsrepository.blob.core.windows.net/sampledata/.

### Cosmos Database

**Do Not share the keys stored in the appsettings.json file publicly.**
The Cosmos database will take approximately 5 minutes to deploy. Upon completion of deployment,
a notification will appear in VS Code and your connection string will be automatically added in
the appsettings.json file. The schema and operations for the Cosmos database are defined in `/backend` folder.
Additional documentation can be found here: [Cosmos Docs](https://github.com/Microsoft/WebTemplateStudio/blob/dev/docs/services/azure-cosmos.md).

### Deployment

If you selected Azure App Service when creating your project, follow these steps:

1. Press `Ctrl + Shift + P` in Windows/Linux or `Shift ⇧ + Command ⌘ + P` in Mac and type/select `Web Template Studio: Deploy App` to start deploying your app.
2. After your project is built, click "Deploy" on the window pop up.
3. Once the deployment is done, click "Browse website" in the notification window on the lower right corner to check out your newly deployed app.

If you did not select Azure App Service and want to create a new Azure App Service web app, follow these steps:

1. Press `Ctrl + Shift + P` in Windows/Linux or `Shift ⇧ + Command ⌘ + P` in Mac and type/select `Tasks: Run Task`, and execute the next tasks:
   - `Install dependencies` to install dependecies in frontend and backend apps.
   - `Publish` to build apps in `publish` folder.
2. Once the build is done, press `Ctrl + Shift + P` in Windows/Linux or `Shift ⇧ + Command ⌘ + P` in Mac and type/select `Azure App Service: Create New Web App...` to create a new web app.
   - Select your subscription
   - Enter your web app name
   - Select Linux as your OS
   - Select Node.js 12 LTS for a Node/Express application, Python 3.7 for a Flask application or .Net Core Latest runtime for ASP .NET application.
3. Once the creation is done, click "Deploy" in the notification window on the lower right corner.
   - Click "Browse" on the top middle section of your screen and select the "publish" folder within your project
   - Click "Yes" in the notification window on the lower right corner (build prompt)
   - Click "Deploy" on the window pop up
   - Click "Yes" in the notification window on the lower right corner again
4. Once the deployment is done, click "Browse website" in the notification window on the lower right corner to check out your newly deployed app.

Consider adding authentication and securing back-end API's by following [Azure App Service Security](https://docs.microsoft.com/en-us/azure/app-service/overview-security).

Full documentation for deployment to Azure App Service can be found here: [Deployment Docs](https://github.com/Microsoft/WebTemplateStudio/blob/dev/docs/deployment.md).

## File Structure

The front-end is based on [create-react-app](https://github.com/facebook/create-react-app). It is served on http://localhost:3000/.

The back-end is based on [ASP.NET Web API](https://dotnet.microsoft.com/apps/aspnet/apis). It is served on https://localhost:5001/.

```
.
├── backend/ - ASP.NET Web Api that provides API routes and serves front-end
│ ├── Contracts/ - Interfaces for services
│ ├── Controllers/ - Handles API calls for routes
│ ├── Models/ - Data models
│ ├── Services/ - Data services
│ │ ├── SampleListService.cs - Contains all interactions with the cosmos database
│ │ ├── SampleDataService.cs - Contains all sample text data for generate pages
│ ├── appsettings.json - Configuration data file
│ ├── Program.cs - Contains create host and run application
│ ├── Startup.cs - Register services and configure application
│ └── WebApi.csproj - Configures Port and HTTP Server
├── frontend/ - React front-end
│ ├── src
│ │ ├── components - React components for each page
│ │ ├── App.jsx - React routing
│ └─└── index.jsx - React root component
└── README.md
```

## Additional Documentation

- React - https://reactjs.org/
- React Router - https://reacttraining.com/react-router/
- Bootstrap CSS - https://getbootstrap.com/
- .NET - https://dotnet.microsoft.com/
- ASP.NET - https://dotnet.microsoft.com/apps/aspnet

- Cosmos DB - https://docs.microsoft.com/en-us/azure/cosmos-db/create-mongodb-dotnet

  This project was created using [Microsoft Web Template Studio](https://github.com/Microsoft/WebTemplateStudio).
