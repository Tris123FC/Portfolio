## Analysis of Homelessness Relief Figures (2024)
**Motivation:** Homelessness is a pressing social issue, and I wanted to understand how government spending impacts homelessness rates across different regions. This project involves a time-series analysis of relief spending relative to housing procurement and a geographical analysis of homelessness figures across the UK. The goal was to identify trends and disparities that could inform policy decisions. 

- **OneDrive Link:**
  [Access Excel File](https://onedrive.live.com/personal/c88ea4021b131a70/_layouts/15/Doc.aspx?resid=C88EA4021B131A70!s4ba9686b3553450bb4dc9e1c5d18dffe&cid=c88ea4021b131a70&migratedtospo=true&app=Excel)

- **Data Source:**
  [UK Government Statistical Data on Homelessness](https://www.gov.uk/government/statistical-data-sets/live-tables-on-homelessness)

![Project Screenshot](images/dashboard.png)

**1. UK Homlessness Rates Across England**

With a new Labour Party government recently elected, building homes is at the top of the agenda as property prices and living costs skyrocket,
all of this is in an effort to reduce purchase and rental costs with intent to alleviate the burden of UK residents.

<img width="4000" alt="image" src="https://github.com/user-attachments/assets/9c516c22-c695-4af7-8b77-9e646313c4f7">

UK house prices reached around £262,000 in 2024 compared to 181,000 in 2007.

source: [Nationwide House Price Index](https://www.nationwidehousepriceindex.co.uk/resources/f/uk-data-series)

<img width="4000" alt="image" src="https://github.com/user-attachments/assets/8fed0525-eaea-4315-9c8e-2e49f0523899">

January 2024 saw an inflation rate of 7%.

source: [ONS Gov UK](https://www.ons.gov.uk/economy/inflationandpriceindices/articles/costoflivinginsights/food)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chart with Textbox and Sources</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .container {
            display: flex;
        }
        .chart {
            width: 60%;
        }
        .textbox {
            width: 35%;
            padding-left: 20px;
        }
        .textbox textarea {
            width: 100%;
            height: 200px;
        }
        footer {
            margin-top: 20px;
        }
        footer ul {
            list-style-type: none;
        }
        footer ul li {
            margin-bottom: 5px;
        }
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <h1>Analysis Report</h1>
        <h2>Chart Visualization and Notes</h2>
    </header>

    <!-- Chart and Textbox Container -->
    <div class="container">
        <!-- Chart Section -->
        <div class="chart">
            <h3>Chart 1: Sales Over Time</h3>
            <!-- Example chart using canvas (you can replace this with an actual chart library) -->
            <canvas id="myChart" width="400" height="400"></canvas>
        </div>

        <!-- Textbox Section -->
        <div class="textbox">
            <h3>Notes</h3>
            <textarea placeholder="Enter your notes here..."></textarea>
        </div>
    </div>

    <!-- Another Section for Additional Charts or Textboxes -->
    <div class="container">
        <div class="chart">
            <h3>Chart 2: Revenue by Region</h3>
            <!-- Example chart using canvas -->
            <canvas id="myChart2" width="400" height="400"></canvas>
        </div>

        <div class="textbox">
            <h3>Notes</h3>
            <textarea placeholder="Enter your notes here..."></textarea>
        </div>
    </div>

    <!-- Footer with Sources -->
    <footer>
        <h3>Sources</h3>
        <ul>
            <li><a href="https://example.com">Source 1: Sales Data</a></li>
            <li><a href="https://example.com">Source 2: Revenue Statistics</a></li>
            <li><a href="https://example.com">Source 3: Market Analysis</a></li>
        </ul>
    </footer>

    <!-- Include Chart.js or other charting library -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        // Chart 1 - Sales Over Time
        var ctx1 = document.getElementById('myChart').getContext('2d');
        var myChart1 = new Chart(ctx1, {
            type: 'line',
            data: {
                labels: ['January', 'February', 'March', 'April', 'May'],
                datasets: [{
                    label: 'Sales',
                    data: [12, 19, 3, 5, 2],
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

        // Chart 2 - Revenue by Region
        var ctx2 = document.getElementById('myChart2').getContext('2d');
        var myChart2 = new Chart(ctx2, {
            type: 'bar',
            data: {
                labels: ['North', 'South', 'East', 'West'],
                datasets: [{
                    label: 'Revenue',
                    data: [10, 15, 7, 12],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    </script>

</body>
</html>
