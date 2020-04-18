# import necessary libaries
import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):

    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) representing the size of the distribution
    """
    def __init__(self, prob=.5, size=20):

        self.p = prob
        self.n = size

        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())





    def calculate_mean(self):
        """Function to calculate the mean from p and n

        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        return self.p * self.n



    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        return math.sqrt(self.n * self.p * (1 - self.p))



    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
        self.n = len(self.data)
        self.p = len([i for i in self.data if i == 1])/len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n


    def plot_bar(self):
        """Function to output a bar chart of the instance variable data using
               matplotlib pyplot library.

               Args:
                   x: value 0 or 1
                   y: number of occurrences of each value

               Returns:
                   None
        """

        plt.bar(x = ['0', '1'], height = [(1 - self.p) * self.n, self.p * self.n])
        plt.xlabel('Value')
        plt.ylabel('Number of Occurrences')
        plt.title('Summary of Value Counts in Data List')
        plt.show()



    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            res(float): probability density function output
        """
        res = math.comb(self.n, k) * (self.p**k) * ((1-self.p)**(self.n-k))
        return res

        pass

    def plot_bar_pdf(self):
        """
        Function to plot the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """
        x = []
        y = []
        for i in range(0,self.n):
            x.append(i)
            y.append(self.pdf(i))
            i += 1

        plt.bar(x, y)
        plt.xlabel('Number of Positive Occurrence')
        plt.ylabel('Probability')
        plt.title('Binomial Probability Distribution Plot')
        plt.show()



    def __add__(self, other):
    # write a method to output the sum of two binomial distributions. Assume both distributions have the same p value.
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        res = Binomial()
        res.mean = self.mean + other.mean
        res.stdev = self.stdev + other.stdev
        res.n = self.n + other.n
        res.p = self.p

        return res


    def __repr__(self):

        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """

        return "mean {}, standard deviation {}, p {}, n {}".format(self.mean, self.stdev, self.p, self.n)

        pass
