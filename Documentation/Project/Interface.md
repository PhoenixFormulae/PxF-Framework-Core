# Interface Design Pattern
The design pattern is MVP (Model-View-Presenter), the
decision to be MVP is due to provide sanity and decoupling
of code, also to make possible unit tests for the 
models and views 


## Model Layer

In this layer lies logic models, in most cases the models
are `Managers`, they are static objects that deal with the
state and functionality of systems, but anything can be
a model.

Keep in mind that models should only talk with `Presenters`
when they want to send messages to or receive messages
from`Views`

## View Layer

In this layer lies the views which are the interface
that users see, they are composed by objects like `Windows`
which have `Controls`

Keep in mind that the `Frames` which are the application
windows that hold the `Views` objects do not come into
consideration in this pattern because they are asbtract
from this scenario


## Presenter Layer

In this layer lies the presenters, they are strictly
objects that are simply responsible to receive/send events
from the view into the model or vice-versa
