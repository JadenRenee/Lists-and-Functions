things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()
print("After capitalizing 'cinderella':", things)
things[0] = things[0].upper()
print("After making 'mozzarella' uppercase:", things)
del things[2]
print("After deleting 'salmonella':", things)
