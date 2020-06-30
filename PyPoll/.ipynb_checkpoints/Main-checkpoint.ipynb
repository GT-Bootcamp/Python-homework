{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "csvpath = os.path.join(\"Resources\", \"election_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Resources\\\\election_data.csv'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "csvpath"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "-------------------------------------\n",
      "Total Votes: 3521000\n",
      "-------------------------------------\n",
      "Correy: 20.0% (704200)\n",
      "Khan: 63.0% (2218230)\n",
      "Li: 14.0% (492940)\n",
      "O'Tooley: 3.0% (105630)\n",
      "-------------------------------------\n",
      "Winner: Khan\n",
      "-------------------------------------\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "39"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "candidates = []\n",
    "votes = 0\n",
    "total_votes = 0\n",
    "candidates = {}\n",
    "candidates_percent = {}\n",
    "winner = \"\"\n",
    "winner_count = 0\n",
    "\n",
    "\n",
    "with open(csvpath, newline=\"\") as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "\n",
    "    csv_header = next(csvfile)\n",
    "    \n",
    "    firstrow = next(csvreader)\n",
    "\n",
    "    for row in csvreader:\n",
    "        total_votes = total_votes + 1\n",
    "        if row[2] in candidates.keys():\n",
    "            candidates[row[2]] += 1\n",
    "        else:\n",
    "            candidates[row[2]] = 1\n",
    "\n",
    "for key, value in candidates.items():\n",
    "    candidates_percent[key] = round((value/total_votes)*100,2)\n",
    "\n",
    "for key in candidates.keys():\n",
    "    if candidates[key] > winner_count:\n",
    "        winner = key\n",
    "        winner_count = candidates[key]\n",
    "\n",
    "print(\"Election Results\")\n",
    "print(\"-------------------------------------\")\n",
    "print(\"Total Votes: \" + str(total_votes))\n",
    "print(\"-------------------------------------\")\n",
    "for key, value in candidates.items():\n",
    "    print(key + \": \" + str(candidates_percent[key]) + \"% (\" + str(value) + \")\")\n",
    "print(\"-------------------------------------\")\n",
    "print(\"Winner: \" + winner)\n",
    "print(\"-------------------------------------\")\n",
    "\n",
    "final_doc = open(\"electioresults.txt\", \"w\")\n",
    "\n",
    "\n",
    "final_doc.write(\"Election Results \\n\")\n",
    "final_doc.write(\"------------------------------------- \\n\")\n",
    "final_doc.write(\"Total Votes: \" + str(total_votes) + \"\\n\")\n",
    "final_doc.write(\"------------------------------------- \\n\")\n",
    "for key, value in candidates.items():\n",
    "    final_doc.write(key + \": \" + str(candidates_percent[key]) + \"% (\" + str(value) + \") \\n\")\n",
    "final_doc.write(\"------------------------------------- \\n\")\n",
    "final_doc.write(\"Winner: \" + winner + \"\\n\")\n",
    "final_doc.write(\"------------------------------------- \\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
