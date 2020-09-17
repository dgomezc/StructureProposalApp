using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.HttpsPolicy;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using System.Security.Authentication;
using MongoDB.Driver;

using ReactAspNet.WebApi.Contracts;
using ReactAspNet.WebApi.Services;


namespace ReactAspNet.WebApi
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllers();
            services.AddSingleton<IMongoClient>(InitializeCosmosClientInstance());
            services.AddSingleton<ISampleListService, SampleListService>();
            services.AddSingleton<ISampleDataService, SampleDataService>();
            services.AddSpaStaticFiles(config => config.RootPath = "ClientApp/build");
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseHttpsRedirection();

            app.UseStaticFiles();
            app.UseSpaStaticFiles();

            app.UseRouting();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });

            if (!env.IsDevelopment())
            {
                app.UseSpa(spa => spa.Options.SourcePath = "ClientApp");
            }
        }

        private IMongoClient InitializeCosmosClientInstance()
        {
            var connectionString = Configuration["COSMOSDB_CONNSTR"];
            var userName = Configuration["COSMOSDB_USER"];
            var dbName = Configuration["COSMOSDB_DB_NAME"];
            var password = Configuration["COSMOSDB_PASSWORD"];

            var settings = MongoClientSettings.FromConnectionString(connectionString);

            var identity = new MongoInternalIdentity(dbName, userName);
            var evidence = new PasswordEvidence(password);
            settings.Credential = new MongoCredential("SCRAM-SHA-1", identity, evidence);

            settings.UseTls = true;
            settings.SslSettings = new SslSettings() { EnabledSslProtocols = SslProtocols.Tls12 };

            return new MongoClient(settings);
        }
    }
}
