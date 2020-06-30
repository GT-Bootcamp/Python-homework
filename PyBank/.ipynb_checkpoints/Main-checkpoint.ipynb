{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "csvpath = os.path.join(\"Resources\", \"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis for file 'budget_data.csv'\n",
      "\n",
      "----------------------------------------------------------\n",
      "\n",
      "    Total Months: 86\n",
      "\n",
      "    Total Revenue: $38382578\n",
      "\n",
      "    Average Revenue Change: $7803\n",
      "\n",
      "    Greatest Increase in Revenue: Feb-2012 ($1926159)\n",
      "\n",
      "    Greatest Decrease in Revenue: Sep-2013 ($-2196167)\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "number_files = 1\n",
    "\n",
    "for numbers in range(number_files):\n",
    "    date = []\n",
    "    revenue =[]\n",
    "    month = []\n",
    "    year =[]\n",
    "    revenueChange =[]\n",
    "    TotalRev =0\n",
    "    TotalRevChange = 0\n",
    "    RevBeg=0\n",
    "    itemCount = 0\n",
    "   \n",
    "\n",
    "    with open(csvpath,'r') as csvFile:\n",
    "        csvReader = csv.reader(csvFile, delimiter=',')\n",
    "       \n",
    "        next(csvReader, None)\n",
    "        \n",
    "        for row in csvReader:        \n",
    "            \n",
    "            itemCount = itemCount + 1\n",
    "            date.append(row[0])\n",
    "            revenue.append(int(row[1]))\n",
    "            TotalRev = TotalRev + int(row[1])\n",
    "            RevEnd = int(row[1])\n",
    "            RevChg = RevEnd - RevBeg\n",
    "            TotalRevChange = TotalRevChange + RevChg\n",
    "            revenueChange.append(RevChg)\n",
    "            splitdate = row[0].split('-')\n",
    "            month.append(str(splitdate[0]))\n",
    "            year.append(splitdate[1][-2:])\n",
    "            RevBeg = RevEnd\n",
    "    \n",
    "    AveRevChg = TotalRevChange / itemCount\n",
    "    GIncrease = max(revenueChange)\n",
    "    GDecrease = min(revenueChange)\n",
    "    IncreaseDate = date[revenueChange.index(GIncrease)]\n",
    "    DecreaseDate = date[revenueChange.index(GDecrease)]\n",
    "    CountM = len(set(date))\n",
    "    \n",
    "    with open('financial_analysis_report_' + str(numbers+1) + '.txt', 'w') as text:\n",
    "        text.write(\"Financial Analysis for file 'budget_data.csv'\"+\"\\n\")\n",
    "        text.write(\"----------------------------------------------------------\\n\")\n",
    "        text.write(\"    Total Months: \" + str(CountM) + \"\\n\")\n",
    "        text.write(\"    Total Revenue: \" + \"$\" + str(TotalRev) +\"\\n\")\n",
    "        text.write(\"    Average Revenue Change: \" + '$' + str(int(AveRevChg)) +'\\n')\n",
    "        text.write(\"    Greatest Increase in Revenue: \" + str(IncreaseDate) + \" ($\" + str(GIncrease) + \")\\n\")\n",
    "        text.write(\"    Greatest Decrease in Revenue: \" + str(DecreaseDate) + \" ($\" + str(GDecrease) + \")\\n\\n\")\n",
    "\n",
    "\t\t\n",
    "print(\"Financial Analysis for file 'budget_data.csv'\"+\"\\n\")\n",
    "print(\"----------------------------------------------------------\\n\")\n",
    "print(\"    Total Months: \" + str(CountM) + \"\\n\")\n",
    "print(\"    Total Revenue: \" + \"$\" + str(TotalRev) +\"\\n\")\n",
    "print(\"    Average Revenue Change: \" + '$' + str(int(AveRevChg)) +'\\n')\n",
    "print(\"    Greatest Increase in Revenue: \" + str(IncreaseDate) + \" ($\" + str(GIncrease) + \")\\n\")\n",
    "print(\"    Greatest Decrease in Revenue: \" + str(DecreaseDate) + \" ($\" + str(GDecrease) + \")\\n\\n\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
