#include <iostream>
#include <sstream>
#include <vector>
#include <numeric>
#include <cmath>
#include <algorithm>

// Helper function to calculate Simple Moving Average (SMA)
double calculateSMA(const std::vector<double>& closes, int period) {
    if (closes.size() < period) return -1;
    return std::accumulate(closes.end() - period, closes.end(), 0.0) / period;
}

// Helper function to calculate Exponential Moving Average (EMA)
double calculateEMA(const std::vector<double>& closes, int period) {
    if (closes.empty()) return -1; 
    double multiplier = 2.0 / (period + 1);
    double ema = closes.front(); 

    for (size_t i = 1; i < closes.size(); i++) {
        ema = (closes[i] - ema) * multiplier + ema;
    }
    return ema;
}

// Helper function to calculate Standard Deviation
double calculateStandardDeviation(const std::vector<double>& closes) {
    if (closes.size() <= 1) return -1; 
    double mean = std::accumulate(closes.begin(), closes.end(), 0.0) / closes.size();
    double sq_sum = std::inner_product(closes.begin(), closes.end(), closes.begin(), 0.0,
                                       [](double sum, double current) { return sum + current; },
                                       [mean](double a, double b) { return (a - mean) * (b - mean); });
    return std::sqrt(sq_sum / (closes.size() - 1));
}

// Helper function to calculate Relative Strength Index (RSI)
double calculateRSI(const std::vector<double>& closes, int period) {
    if (closes.size() < period) return -1; 

    double gains = 0.0, losses = 0.0;
    for (size_t i = 1; i < period; ++i) {
        double difference = closes[i] - closes[i - 1];
        if (difference > 0) gains += difference;
        else losses -= difference;
    }

    if (losses == 0) return 100; 

    double rs = gains / losses;
    return 100 - (100 / (1 + rs));
}

// Helper function to calculate Maximum Drawdown (MDD)
double calculateMDD(const std::vector<double>& equityCurve) {
    double peak = -std::numeric_limits<double>::infinity();
    double maxDrawdown = 0.0;

    for (double value : equityCurve) {
        if (value > peak) peak = value;
        double drawdown = peak - value;
        if (drawdown > maxDrawdown) maxDrawdown = drawdown;
    }

    return maxDrawdown;
}

int main() {
    std::string line;
    std::vector<double> closes;

    while (std::getline(std::cin, line)) {
        std::istringstream iss(line);
        double close;
        if (iss >> close) {
            closes.push_back(close);
        }
    }

    double sma = calculateSMA(closes, 5); 
    double ema = calculateEMA(closes, 5); 
    double stdDev = calculateStandardDeviation(closes);
    double rsi = calculateRSI(closes, 14); 
    double mdd = calculateMDD(closes);

    std::cout << "SMA: " << sma << std::endl;
    std::cout << "EMA: " << ema << std::endl;
    std::cout << "Standard Deviation: " << stdDev << std::endl;
    std::cout << "RSI: " << rsi << std::endl;
    std::cout << "MDD: " << mdd << std::endl;

    return 0;
}
