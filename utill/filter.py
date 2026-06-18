from utill.bean import Activity
import datetime
from abc import ABC, abstractmethod
from enum import Enum
from .bean import filt_method


def filt_acts(acts: list[Activity], filter: filter) -> list[Activity]:
    return [act for act in acts if filter.filt(act)]


class filter(ABC):
    @abstractmethod
    def filt(self, act: Activity) -> bool:
        pass


class all_true(filter):
    def __init__(self):
        super().__init__()

    def filt(self, act: Activity) -> bool:
        return True


class filter_super(filter):
    def __init__(self, filter: filter = None):
        super().__init__()
        self.filter = filter

    def decorate(self, filter: filter):
        self.filter = filter
        return self

    def filt(self, act: Activity) -> bool:
        return self.filter.filt(act)

    def print(self):
        if self.filter:
            self.filter.print()
        # print(self.__class__.__name__)


class filter_by_capacity(filter_super):
    def __init__(self):
        super().__init__()

    def filt(self, act: Activity) -> bool:
        # print(act.allow_user_count, act.join_user_count)
        if act.allow_user_count <= act.join_user_count:
            return False
        return super().filt(act)


class filter_by_has_join(filter_super):
    def __init__(self, has_join=1):
        super().__init__()
        self.has_join = has_join

    def filt(self, act: Activity) -> bool:
        # print(act.has_join)
        return act.has_join == self.has_join and super().filt(act)


class filter_by_join_end_time(filter_super):
    def __init__(self):
        super().__init__()

    def filt(self, act: Activity) -> bool:
        # print(act.join_start_time, act.join_end_time)
        now = datetime.datetime.now()
        return act.join_end_time > now and super().filt(act)


class filter_by_start_time(filter_super):
    def __init__(self):
        super().__init__()

    def filt(self, act: Activity) -> bool:
        # print(act.start_time)
        now = datetime.datetime.now()
        return act.start_time > now and super().filt(act)


class filter_by_category(filter_super):
    def __init__(self, categories: list[str]):
        super().__init__()
        self.categories = categories

    def filt(self, act: Activity) -> bool:
        # print(act.category_name)
        for cate in self.categories:
            if cate in act.category_name:
                return super().filt(act)
        return False


class filter_by_credit(filter_super):
    def __init__(self, credit: float):
        super().__init__()
        self.credit = credit

    def filt(self, act: Activity) -> bool:
        # print(act.credit)
        return self.credit <= act.credit and super().filt(act)


class filter_by_tribe(filter_super):
    def __init__(self, tribe: str):
        super().__init__()
        self.tribe = tribe

    def filt(self, act: Activity) -> bool:
        # print(act.allow_tribe)
        return (
            not act.allow_tribe or self.tribe in act.allow_tribe and super().filt(act)
        )


class filter_by_join_type(filter_super):
    def __init__(self, join_type=1):
        super().__init__()
        self.join_type = join_type

    def filt(self, act: Activity) -> bool:
        # print(act.join_type)
        return self.join_type == act.join_type and super().filt(act)


class filter_by_grade(filter_super):
    def __init__(self, grade: str):
        super().__init__()
        self.grade = grade

    def filt(self, act: Activity) -> bool:
        # print(act.allow_year)
        return (
            not act.allow_year
            or not self.grade
            or self.grade in [str(year) for year in act.allow_year]
        ) and super().filt(act)


class filter_by_college(filter_super):
    def __init__(self, college: str):
        super().__init__()
        self.college = college

    def filt(self, act: Activity) -> bool:
        # print(act.allow_college)
        return (
            not act.allow_college
            or not self.college
            or self.college in act.allow_college
        ) and super().filt(act)


class filt_context:
    def __init__(self, filt_methods: list[filt_method], **kwargs):
        self.set_filter_method(filt_methods, **kwargs)

    def set_filter_method(self, filt_methods: list[filt_method], **kwargs):
        self.filter: filter = all_true()
        for method in filt_methods:
            if method == filt_method.default_filt:
                pass
            elif method == filt_method.filt_by_capacity:
                self.filter = filter_by_capacity().decorate(self.filter)
            elif method == filt_method.filt_by_has_join:
                self.filter = filter_by_has_join().decorate(self.filter)
            elif method == filt_method.filt_by_join_end_time:
                self.filter = filter_by_join_end_time().decorate(self.filter)
            elif method == filt_method.filt_by_category:
                # print("categotires" + kwargs.get("categories", None))
                self.filter = filter_by_category(
                    kwargs.get("categories", None)
                ).decorate(self.filter)
            elif method == filt_method.filt_by_grade:
                self.filter = filter_by_grade(kwargs.get("grade", None)).decorate(
                    self.filter
                )
            elif method == filt_method.filt_by_college:
                self.filter = filter_by_college(kwargs.get("college", None)).decorate(
                    self.filter
                )
            elif method == filt_method.filt_by_tribe:
                self.filter = filter_by_tribe(kwargs.get("tribe")).decorate(self.filter)
            elif method == filt_method.filt_by_join_type:
                self.filter = filter_by_join_type().decorate(self.filter)
            else:
                print(f"filt_context.__init__ Error: 未知的filt_method: {method}")
        self.filt_methods = filt_methods

    def set_filter(self, filter: filter):
        self.filter = filter
        self.filt_methods = None

    def get_filter(self) -> filter:
        return self.filter

    def get_filt_methods(self) -> list[filt_method]:
        return self.filt_methods

    def filt(self, act: Activity) -> bool:
        return self.filter.filt(act)

    def filt_acts(self, acts: list[Activity]) -> list[Activity]:
        return [act for act in acts if self.filt(act)]
