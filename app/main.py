from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    hall = CinemaHall(hall_number)
    cleaner_peop = Cleaner(cleaner)
    obj_customer = []
    for person in customers:
        new_person = Customer(name=person["name"], food=person["food"])
        obj_customer.append(new_person)
    for person in obj_customer:
        CinemaBar.sell_product(product=person.food, customer=person)
    hall.movie_session(movie, obj_customer, cleaner_peop)
