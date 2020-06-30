{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lower case characters:  14\n",
      "Upper case characters:  2\n"
     ]
    }
   ],
   "source": [
    "s = \"Always and Forever\"\n",
    "l,u = 0,0\n",
    "for i in s: \n",
    "    if (i>='a'and i<='z'): \n",
    "        l=l+1           \n",
    "    if (i>='A'and i<='Z'):\n",
    "        u=u+1                 \n",
    "print('Lower case characters: ',l) \n",
    "print('Upper case characters: ',u)"
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
