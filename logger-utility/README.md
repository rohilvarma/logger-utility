# Logger Utility
This repo is a hands on project to learn Low Level Design. I have created this small project to refine and iron my understanding of the SOLID principles.

## Understanding
The basic idea is to understand SOLID and so I have designated the `logger.py` as the main high level function that is going to be close to the business logic.

I have created an abstract class within the `writer.py` called `LogWriter`. This class is responsible to handle writing into different kinds of outputs.
Currently it supports writing on Terminal and File, whose functions are defined in their respective classes, `terminal.py` and `file.py`. 
This is division of different output writers is in accordance with
 - **SRP** - All the classes follow a single responsibility and are tightly coupled.
 - **OCP** - New writers can be easily added without having to modify any existing code.
 - **LSP** - All the classes are children of `LogWriter` class. And the client is not dependent on the type of caller it is invoking the functions on, ie, all writers inherit from `LogWriter` and can be used interchangeably.
 - **ISP** - Since `LogWriter` only exposes the methods needed by all the writers, we are in accordance with **ISP**.
 - **DIP** - `logger.py` a high level component, close to the business logic is not dependent upon the low-level components that actually do the job, ie, `terminal.py` and `file.py`. But instead is dependent on the `config.py`. This dependency decouples the `logger.py` from the details of low level implementation and thus this separation of concerns implements DIP in logger utility. 

## ToDo
- [ ] Add a ranking system in the severity of the logs
- [ ] Complete file writer
- [ ] Test the logger class