using webapp.Data;

namespace csd_tests;

using System;
using Xunit;
using System.Linq;
using System.Threading.Tasks;

public class WeatherForecastServiceTest
{
    private readonly WeatherForecastService _weatherForecastService;

    public WeatherForecastServiceTest()
    {
        _weatherForecastService = new WeatherForecastService();
    }

    [Fact]
    public async Task GetForecastAsync_ReturnsCorrectNumber()
    {
        var startDate = new DateOnly(2023, 3, 21);
        var forecasts = await _weatherForecastService.GetForecastAsync(startDate);
        Assert.Equal(5, forecasts.Length);
    }

    [Fact]
    public async Task GetForecastAsync_ReturnsCorrectDate()
    {
        var startDate = new DateOnly(2023, 3, 21);
        var forecasts = await _weatherForecastService.GetForecastAsync(startDate);
        Assert.Equal(startDate.AddDays(1), forecasts[0].Date);
        Assert.Equal(startDate.AddDays(2), forecasts[1].Date);
        Assert.Equal(startDate.AddDays(3), forecasts[2].Date);
        Assert.Equal(startDate.AddDays(4), forecasts[3].Date);
        Assert.Equal(startDate.AddDays(5), forecasts[4].Date);
    }

    [Fact]
    public async Task GetForecastAsync_ReturnsCorrectTemperatureRange()
    {
        var startDate = new DateOnly(2023, 3, 21);
        var forecasts = await _weatherForecastService.GetForecastAsync(startDate);
        foreach (var forecast in forecasts)
        {
            Assert.InRange(forecast.TemperatureC, -20, 55);
        }
    }
}