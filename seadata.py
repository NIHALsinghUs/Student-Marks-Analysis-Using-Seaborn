# Import Pandas library for data handling
import pandas as pd

# Import Seaborn library for data visualization
import seaborn as sns

# Import Matplotlib library for plotting graphs
import matplotlib.pyplot as plt

# Display project title
print("--- Student Marks Analysis Using Seaborn ---")

# Create an empty DataFrame with required columns
data = pd.DataFrame(columns=["Name" , "Maths" , "Science" , "English"])

# Loop to continuously add student records
while True:
    
    # Display separator line
    print("-----------------------------------")

    # Take student name as input
    name = input("Enter the Student Name : ")
    
    # Take Maths marks as input
    maths = int(input("Enter the Marks of Maths : "))
    
    # Take Science marks as input
    science = int(input("Enter the Marks of Science : "))
    
    # Take English marks as input
    english = int(input("Enter the Marks of English : "))

    # Add student data to DataFrame
    data.loc[len(data)] = [name , maths , science , english]

    # Display current DataFrame without index
    print(data.to_string(index = False))
    
    # Display separator line
    print("-----------------------------------")

    # Ask user whether to add another student
    choice = input("Add another student? (y/n): ")

    # Save data and exit loop if user enters 'n'
    if choice.lower() == 'n':
        
        # Save DataFrame to CSV file
        data.to_csv("student_data.csv")
        
        # Exit input loop
        break

    # Display separator line
    print("-----------------------------------")

# Calculate average marks for each student
data["Average"] = data[["Maths" , "Science" , "English"]].mean(axis=1)

# Display updated DataFrame with Average column
print(data)

# Display separator line
print("-----------------------------------")

# Main visualization menu loop
while True:

    # Display menu options
    print('1. Display Bar plot') 
    print('2. Display Histogram plot')
    print('3. Display Heatmap')
    print("4. Exit")

    # Display separator line
    print("-----------------------------------")

    # Take user choice
    userchoice = int(input("Enter the option : "))

    # Display Bar Plot
    if (userchoice == 1):

        # Create bar plot of student average marks
        sns.barplot(x = "Name" , 
                    y = "Average" , 
                    data = data , 
                    palette=["red", "blue", "green", "yellow", "orange", "purple", "pink"])
        
        # Set graph title
        plt.title("Student Average Marks")
        
        # Set x-axis label
        plt.xlabel("Student Name")
        
        # Set y-axis label
        plt.ylabel("Average Marks")
        
        # Save graph as image
        plt.savefig("bar_img.png")
        
        # Display graph
        plt.show()

    # Display Histogram
    elif (userchoice == 2):

        # Create histogram of average marks
        sns.histplot(x = "Average" , 
                    data = data , 
                    kde = True , 
                    bins = 7 )
        
        # Set graph title
        plt.title("Average Marks Distribution")
        
        # Set x-axis label
        plt.xlabel("Average Marks")
        
        # Set y-axis label
        plt.ylabel("Frequency")
        
        # Save graph as image
        plt.savefig("his_img.png")
        
        # Display graph
        plt.show()

    # Display Heatmap
    elif (userchoice == 3):

        # Create correlation heatmap
        sns.heatmap(data.corr(numeric_only=True) , annot = True)

        # Set graph title
        plt.title("Student Marks Correlation Heatmap")
        
        # Save graph as image
        plt.savefig("heat_img.png")
        
        # Display graph
        plt.show()

    # Exit program
    elif (userchoice == 4):
        break

    # Handle invalid menu choices
    else:
        print("Invalid Option Try Again")