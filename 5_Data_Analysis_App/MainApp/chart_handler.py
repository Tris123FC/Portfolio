class ChartHandler:
    def create_scatter_plot(self, modified_df):
        sorted_df = modified_df.sort_values(by=self.column1)
        plt.figure(figsize=(3, 2))
        plt.scatter(sorted_df[self.column1], sorted_df[self.column2], label='Y1', marker='o')
        plt.title('Two-Dimensional Scatter Plot')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.grid()

        return plt.gcf()

    def plot_chart(self, selected_chart):
        if self.modified_df is not None:
            if selected_chart == 'line chart':
                fig = self.create_line_chart(self.modified_df)
                canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
                canvas.draw()
                canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
                self.chart_frame.grid_rowconfigure(0, weight=1)
                self.chart_frame.grid_columnconfigure(0, weight=1)
            if selected_chart == 'scatter plot':
                fig = self.create_scatter_plot(self.modified_df)
                canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
                canvas.draw()
                canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
                self.chart_frame.grid_rowconfigure(0, weight=1)
                self.chart_frame.grid_columnconfigure(0, weight=1)