#アソシエーション分析
# https://qiita.com/haruhiko28/items/dd9555ad0aba01b8d8a3
# https://www.albert2005.co.jp/knowledge/marketing/customer_product_analysis/abc_association

import json
import pyfpgrowth

txt = [["",""],["",""]]
patterns = []

for i,categories in enumerate(txt):
  if i > 200:break
  patterns.append(categories)
  

frequent_patterns = pyfpgrowth.find_frequent_patterns(patterns, 3)
association_rules = pyfpgrowth.generate_association_rules(frequent_patterns, 0.7)
for a,b in sorted(frequent_patterns.items(), key=lambda x: -x[1]):
  rows = [b]+ list(a)
  print(rows)
print("===")
print(association_rules)
