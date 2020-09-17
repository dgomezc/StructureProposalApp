using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using MongoDB.Bson;
using MongoDB.Driver;
using Microsoft.Extensions.Configuration;
using ReactAspNet.WebApi.Contracts;
using ReactAspNet.WebApi.Models;

namespace ReactAspNet.WebApi.Services
{
    public class SampleListService : ISampleListService
    {
        private readonly IMongoCollection<ListItem> items;

        public SampleListService(IMongoClient client, IConfiguration config)
        {
            string databaseName = config["COSMOSDB_DB_NAME"];
            string collectionName = config["COSMOSDB_COLLECTION_NAME"];
            var mongoDb = client.GetDatabase(databaseName);
            items = mongoDb.GetCollection<ListItem>(collectionName);
        }

        public async Task<ListItem> AddItemAsync(ListItem item)
        {
            await items.InsertOneAsync(item);
            return item;
        }

        public async Task<long> DeleteItemAsync(string id)
        {
            var data = Builders<ListItem>.Filter.Eq("Id", id);
            var result = await items.DeleteOneAsync(data);
            return result.DeletedCount;
        }

        public async Task<IEnumerable<ListItem>> GetItemsAsync()
        {
            return await items.Find(_ => true).ToListAsync();
        }
    }
}
