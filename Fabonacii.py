num1 = 1; 
num2 = 1;
fabSeriesArray = [];
fabSeriesArray.append(num1);
fabSeriesArray.append(num2);
index = 0;
fabSeriesTotalSum = 0;
fabSeries = 0;
while 1:
    fabSeries = num1 + num2;
    if fabSeries < 4000000:
        fabSeriesArray.append(fabSeries);	
        num1 = num2;
        num2 = fabSeries;
        index += 1;
        if fabSeries % 2 == 0:
            fabSeriesTotalSum = fabSeriesTotalSum + fabSeries;
            print(fabSeriesTotalSum);
    else:
	    break; 

