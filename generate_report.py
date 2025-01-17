import csv
import yfinance as yf
import matplotlib.pyplot as plt


def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    price = stock.history(period="1d")['Close'].iloc[-1]
    return round(price, 2)

def load_portfolio(file_path):
    portfolio = []
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader) 
        for row in csv_reader:
            portfolio.append({
                "symbol": row[0],
                "quantity": float(row[1]),
                "purchase_price": float(row[2]),
            })
    return portfolio

def update_portfolio(portfolio):
    for stock in portfolio:
        stock["current_price"] = get_stock_price(stock["symbol"])
        stock["current_value"] = stock["current_price"] * stock["quantity"]
        stock["profit_loss"] = stock["current_value"] - (stock["quantity"] * stock["purchase_price"])
        stock["percentage_change"] = (stock["profit_loss"] / (stock["quantity"] * stock["purchase_price"])) * 100
    return portfolio

def create_pie_chart(portfolio, output_file="portfolio_chart.png"):
    labels = [stock["symbol"] for stock in portfolio]
    sizes = [stock["current_value"] for stock in portfolio]
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
    plt.title("Portfolio Distribution")
    plt.savefig(output_file)
    plt.close()

def create_html_report(portfolio, chart_file="portfolio_chart.png", output_file="portfolio.html"):
    with open("index.html", "r") as template_file:
        html_template = template_file.read()
    table_rows = ""
    for stock in portfolio:
        row_class = "profit" if stock["profit_loss"] >= 0 else "loss"
        table_rows += f"""
            <tr>
                <td>{stock['symbol']}</td>
                <td>{stock['quantity']}</td>
                <td>${stock['purchase_price']}</td>
                <td>${stock['current_price']}</td>
                <td>${stock['current_value']:.2f}</td>
                <td class="{row_class}">${stock['profit_loss']:.2f}</td>
                <td class="{row_class}">{stock['percentage_change']:.2f}%</td>
            </tr>
        """
    html_report = html_template.replace("{{table_rows}}", table_rows)
    html_report = html_report.replace("{{chart_file}}", chart_file)

    with open(output_file, "w") as file:
        file.write(html_report)
    print(f"Portfolio report has been saved to {output_file}")

portfolio = load_portfolio("portfolio.csv")
updated_portfolio = update_portfolio(portfolio)
create_pie_chart(updated_portfolio)
create_html_report(updated_portfolio)
