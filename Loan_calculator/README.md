This project is about creating a loan calculator for annuity and differentiated payment
Overview: 
1/ Annuity payment is a fixed amount of payment that you will pay every period
2/ Differentiated payment is paying a decreasing amount of payment throughout loan's life
This project mainly practices using command line interface for input parameter value, which involves:
1/ Setting up: Creating parser and add arguments
2/ Command checking 
2.1/ Need 4/5 parameters
2.2/ Type parameters must be either diff or annuity
2.3/ If type if diff, then payment must not be assigned
2.4/ None of parameters accept negative values
3/ Annuity payment: Calculating the lacking parameter by using provided ones
4/ Diff payment: Calculating payment for every month
6/ Calculate overpayment (total paid interest): total payment - principal
