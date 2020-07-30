using System.Collections.Generic;
using ReactAspNet.WebApi.Models;

namespace ReactAspNet.WebApi.Contracts
{
    public interface ISampleDataService
    {
        IEnumerable<SampleCompany> GetSampleCompanies();
    }
}
