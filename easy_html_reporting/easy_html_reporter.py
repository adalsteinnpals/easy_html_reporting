# -*- coding: utf-8 -*-
"""
Created on Wed May  9 23:16:48 2018

@author: adals
"""

#%%

import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mpld3
from mpld3 import plugins
import webbrowser


class easy_reporter():
    def __init__(self):
        self.possible_configs = ['h1','h2','h3','h4','h5','h6','p']
        self.html_string = ""
        self.html_table = ["""<div style="overflow-x:auto;">""","</div>"]
        self.html_style = """<style>
                        * {
                          -webkit-box-sizing: border-box;
                          box-sizing: border-box;
                          text-rendering: optimizeLegibility;
                          -webkit-font-smoothing: antialiased;
                          -moz-osx-font-smoothing: grayscale;
                          font-kerning: auto;
                        }
                        
                        
                        table {
                            border-collapse: collapse;
                            border: none;
                            width: 100%;
                        }
                        
                        th, td {
                            text-align: left;
                            padding: 8px;
                            white-space: nowrap;
                        }
                        
                        tr:nth-child(even){background-color: #f2f2f2}
                            
                            
                        html {
                          font-size: 12pt;
                          line-height: 1.4;
                          font-weight: 400;
                          font-family: 'Helvetica Neue', 'Myriad Pro', 'Segoe UI', Myriad, Helvetica, 'Lucida Grande', 'DejaVu Sans Condensed', 'Liberation Sans', 'Nimbus Sans L', Tahoma, Geneva, Arial, sans-serif;
                        }
                        body {
                          padding: 1em;
                          margin: 0 auto;
                          max-width: 800px;
                        }
                        code,
                        pre,
                        blockquote {
                          padding: .2em;
                          background: rgba(0,0,0,.1);
                        }
                        code,
                        pre {
                          font-family: Consolas, "Andale Mono WT", "Andale Mono", "Lucida Console", "Lucida Sans Typewriter", "DejaVu Sans Mono", "Bitstream Vera Sans Mono", "Liberation Mono", "Nimbus Mono L", Monaco, "Courier New", Courier, monospace;
                        }
                        h1, h2, h3, h4, h5, h6 {
                          margin: 0 0 .5em 0;
                          line-height: 1.2;
                          letter-spacing: -.02em;
                        }
                        [class*=float-] {
                          margin: 0 auto 1em auto;
                          display: block;
                          width: auto;
                          max-width: 100%;
                          clear: both;
                        }
                        @media (min-width: 600px) {
                          h1 { font-size: 300%; }
                          h2 { font-size: 200%; }
                          h3 { font-size: 180%; }
                          h4 { font-size: 160%; }
                          h5 { font-size: 140%; }
                          h6 { font-size: 120%; }
                          [class*=float-] {
                            max-width: 40%;
                          }
                          .float-left {
                            float: left;
                            margin: 0 1em .5em 0;
                          }
                          .float-right {
                            float: right;
                            margin: 0 0 .5em 1em;
                          }
                        }
                        </style>"""
    def add_text(self, html_type, text):
        if html_type in self.possible_configs:
            self.html_string = self.html_string+"<"+html_type+">"+text+"</"+html_type+">"
    def headline(self,headline):
        self.html_string = self.html_string+"<h1>"+headline+"</h1>"
    def header(self, header):
        self.html_string = self.html_string+"<h2>"+header+"</h2>"
    def string(self, s):
        self.html_string = self.html_string+"<p>"+s+"</p>"
    def table_from_pandas(self, pd_table):
        self.html_string = self.html_string+self.html_table[0]+pd_table.to_html()+self.html_table[1]
    def figure(self, fig):
        self.html_string = self.html_string+mpld3.fig_to_html(fig)
    def generate_html_string(self):
        return "<html><head>"+self.html_style+"</head><body>"+self.html_string+"</body></html>"
    def save_and_open_html(self, html_name):
        file_name = html_name+'.html'
        f = open(file_name,'w')
        f.write(self.generate_html_string())
        f.close()
        webbrowser.open_new_tab(file_name)
    def run_example(self):
        fig, ax = plt.subplots()
        ax.plot(np.random.rand(100))
        plt.title('Figure1')
        
        
        fig2, ax2 = plt.subplots()
        ax2.plot(np.random.rand(100))
        plt.title('Figure2')
        
        rc = easy_reporter()   
        rc.headline('EXPERIMENTS')  
        rc.add_text('p',"""This package was made to create simple "report-like" html files for
                    for easy integration with pandas and matplotlib with mpld3""")
        rc.add_text('h1','Experiment1')  
        rc.add_text('p','In this experiment we did a lot of things')
        rc.table_from_pandas(pd.DataFrame(np.random.rand(5,5)))
        rc.figure(fig)
        rc.header('Experiment2')  
        rc.string('In this experiment we did a few things')
        rc.figure(fig2)
        rc.save_and_open_html('test_experiment')
            

if __name__ == "__main__":
    er = easy_reporter()
    er.run_example()


