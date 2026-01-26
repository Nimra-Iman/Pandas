# they are used for reshaping dataframes
import pandas as pd
df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',
                           'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6],
                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
print(df)
print(df.shape)  #(6, 4) yani df m 6 rows hn or 4 columns hn
#-------> One way to reshape dataframes is to use pivot:
# in pivot, one column is set as index, one column is set as column name and other
# columns are used for representing actual dataset but you can use one column
# as well.
new=pd.pivot(df, index="foo", columns="bar")
new=pd.pivot(df, index="foo", columns="bar", values="baz")  #esa krny s dataset5 m just 
                                # bax ki values show hon gi
# print(new)
# THERE CANNOT BE A DUPLICATE VALUES IN INDEX IN PIVOT BUT PIVOT-TABLE CAN HAVE.

print()
print()
# ----- pivot-table:   (is ka advantage y h k hm ek s ziada indexes de skty hn or
                # y achy s manage kr leta h)
n=df.pivot_table( index=["foo",'bar'], columns='zoo')
print(n)
print()
print()
print()

# -----------  melt  ---------------------------------------------
print(pd.melt(df, id_vars='foo', var_name="vaaarss" ))