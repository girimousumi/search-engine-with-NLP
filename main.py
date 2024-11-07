import tkinter as tk
from tkinter import scrolledtext
from search import search_query

class SearchEngineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Search Engine")

        # Query input
        self.query_label = tk.Label(root, text="Enter your search query:")
        self.query_label.pack(pady=10)
        
        self.query_entry = tk.Entry(root, width=50)
        self.query_entry.pack(pady=5)

        # Search button
        self.search_button = tk.Button(root, text="Search", command=self.perform_search)
        self.search_button.pack(pady=10)

        # Results display
        self.results_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
        self.results_text.pack(pady=10)

    def perform_search(self):
        query = self.query_entry.get()
        if query:
            results = search_query(query)
            self.results_text.delete(1.0, tk.END)
            if results:
                for doc_name, score in results:
                    self.results_text.insert(tk.END, f"{doc_name} - Score: {score:.4f}\n")
            else:
                self.results_text.insert(tk.END, "No relevant documents found.")
        else:
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "Please enter a query.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SearchEngineApp(root)
    root.mainloop()
