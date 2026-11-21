#dictionary initilaization
#yesma dic bitra dic use gareko xa
fees ={"everest":{"nepali":100, "saarc":1500, "foreign":3000},
       "annapurna":{"nepali":100, "saarc":1000, "foreign": 3000},
       "langtang":{"nepali":100, "saarc":1500,"foreign":3000}}

 #storing toursits ko info
 #yesma hamiley list ra tuple use gareko xauma 
 #jasma list chhai multiple value store gran ko lagi 
 #tuple chahi order way ma value rakhna ko lagi
# yesma chahi mailey name, nationality, ra age and area ko name lekheko xu
visitors= [("aarav", "nepali", 22, "everest"),
           ("emma","foreign", 34, "annapurna"),
           ("rahul", "saarc", 8, "langtang"),
           ("john", "foreign", 65, "everest"),
           ("mina", "nepali", 30, "annapurna"),
           ("li", "foreign", 28, "everest")
           ]

#aaba ma initilaize garxu revenue ra visitors count
#yo bhaneko dict lai initialization gareko
#jasma yesko value initially 0 hunxa
#0 kina gareko bhanda yedi kunai thau add garnu parda tesko value ni 0 nai hoos initially 
revenue = {area:0 for area in fees} 
visitor_count= {area:0 for area in fees} 
categories= set() #set chahi kina gareko bhanda duplicate value remove garna


#permit fees chahi calculate garne
print("nepal tourism- trekking permit report")
print("-----------------")

for name, category, age, area in visitors:
    #original fee lai get garna
    fee = fees[area][category]

    #age discount
    if age<10:
        fee = 0

    elif age>=60:
        fee = fee//2

        #display
    print(f"{name:<6} {area:<10} {fee:>7}")

    #claculate area revenue
    revenue[area]+= fee

    #count visitors
    visitor_count[area]+= 1

#store unique categories
    categories.add(category)

#max count garna ko lagiml;l
    busiest_area = max(visitor_count,key= visitor_count.get)
    total_revenue = sum(revenue.values())

    print("\nrevenue by area:", revenue)
    print(
    "Busiest area:",
    busiest_area,
    f"({visitor_count[busiest_area]} visitors)"
)

print("Visitor categories:", sorted(categories))

print("Total revenue: Rs", total_revenue)




    


