import pytest
from src.fact_fibo.factorial import factorial
from src.fact_fibo.factorial_recursive import factorial_recursive
from src.fact_fibo.fibo import fibo
from src.fact_fibo.fibo_recursive import fibo_recursive
from src.sorting.bubble_sort import bubble_sort
from src.sorting.quick_sort import quick_sort
from src.sorting.counting_sort import counting_sort
from src.sorting.radix_sort import radix_sort
from src.sorting.bucket_sort import bucket_sort
from src.sorting.heap_sort import heap_sort
from src.stack.stack import Stack


class TestFactorial:
    """Тесты для функций факториала"""

    def test_factorial_normal_cases(self):
        """Тест факториала для стандартных случаев"""
        assert factorial(3) == 6
        assert factorial(7) == 5040
        assert factorial(0) == 1
        assert factorial(4) == 24

        assert factorial_recursive(3) == 6
        assert factorial_recursive(7) == 5040
        assert factorial_recursive(0) == 1
        assert factorial_recursive(4) == 24

    def test_factorial_invalid_input(self):
        """Тест факториала для некорректного ввода"""
        with pytest.raises(ValueError):
            factorial(-2)
        with pytest.raises(ValueError):
            factorial(-10)
        with pytest.raises(ValueError):
            factorial_recursive(-3)
        with pytest.raises(ValueError):
            factorial_recursive(-8)


class TestFibonacci:
    """Тесты для функций чисел Фибоначчи"""

    def test_fibo_middle_values(self):
        """Тест чисел Фибоначчи для средних значений"""
        assert fibo(1) == 1
        assert fibo(4) == 3
        assert fibo(7) == 13
        assert fibo(5) == 5

        assert fibo_recursive(1) == 1
        assert fibo_recursive(4) == 3
        assert fibo_recursive(7) == 13
        assert fibo_recursive(5) == 5


    def test_fibo_invalid_input(self):
        """Тест чисел Фибоначчи для некорректного ввода"""
        with pytest.raises(ValueError):
            fibo(0)
        with pytest.raises(ValueError):
            fibo(-1)
        with pytest.raises(ValueError):
            fibo_recursive(0)
        with pytest.raises(ValueError):
            fibo_recursive(-3)


class TestSortingAlgorithms:
    """Тесты для алгоритмов сортировки"""

    def test_bubble_sort_variations(self):
        """Тест пузырьковой сортировки с разными наборами"""
        assert bubble_sort(['7', '2', '7', '2', '1', '7']) == ['1', '2', '2', '7', '7', '7']
        assert bubble_sort(['4', '1']) == ['1', '4']
        assert bubble_sort(['2', '4', '6', '8']) == ['2', '4', '6', '8']
        assert bubble_sort(['15', '3', '28', '7', '12', '1']) == ['1', '3', '7', '12', '15', '28']
        assert bubble_sort([]) == []

    def test_quick_sort_variations(self):
        """Тест быстрой сортировки с разными наборами"""
        assert quick_sort(['7', '2', '7', '2', '1', '7']) == ['1', '2', '2', '7', '7', '7']
        assert quick_sort(['9', '7', '5', '3']) == ['3', '5', '7', '9']
        assert quick_sort(['9']) == ['9']
        assert quick_sort(['15', '3', '28', '7', '12', '1']) == ['1', '3', '7', '12', '15', '28']

    def test_counting_sort_variations(self):
        """Тест сортировки подсчетом с разными наборами"""
        assert counting_sort(['4', '1']) == ['1', '4']
        assert counting_sort(['2', '4', '6', '8']) == ['2', '4', '6', '8']
        assert counting_sort(['7', '2', '7', '2', '1', '7']) == ['1', '2', '2', '7', '7', '7']
        assert counting_sort([]) == []

    def test_radix_sort_variations(self):
        """Тест поразрядной сортировки с разными наборами"""
        assert radix_sort(['15', '3', '28', '7', '12', '1']) == ['1', '3', '7', '12', '15', '28']
        assert radix_sort(['2', '4', '6', '8']) == ['2', '4', '6', '8']
        assert radix_sort(['9', '7', '5', '3']) == ['3', '5', '7', '9']
        assert radix_sort(['9']) == ['9']

    def test_bucket_sort_variations(self):
        """Тест блочной сортировки с разными наборами"""
        assert bucket_sort(['4', '1']) == ['1', '4']
        assert bucket_sort(['7', '2', '7', '2', '1', '7']) == ['1', '2', '2', '7', '7', '7']
        assert bucket_sort(['2', '4', '6', '8']) == ['2', '4', '6', '8']
        assert bucket_sort([]) == []

    def test_heap_sort_variations(self):
        """Тест пирамидальной сортировки с разными наборами"""
        assert heap_sort(['15', '3', '28', '7', '12', '1']) == ['1', '3', '7', '12', '15', '28']
        assert heap_sort(['9', '7', '5', '3']) == ['3', '5', '7', '9']
        assert heap_sort(['9']) == ['9']
        assert heap_sort(['7', '2', '7', '2', '1', '7']) == ['1', '2', '2', '7', '7', '7']


class TestStackOperations:
    """Тесты для операций со стеком"""

    @pytest.fixture
    def fresh_stack(self):
        """Фикстура для создания нового стека"""
        return Stack()

    def test_basic_stack_operations(self, fresh_stack):
        """Тест базовых операций со стеком"""
        fresh_stack.push("1")
        fresh_stack.push("2")
        fresh_stack.push("3")

        assert fresh_stack.peek() == "3"
        assert len(fresh_stack) == 3
        assert fresh_stack.is_empty() == False

        assert fresh_stack.pop() == "3"
        assert fresh_stack.pop() == "2"
        assert fresh_stack.pop() == "1"

        assert fresh_stack.is_empty() == True

    def test_stack_alternating_operations(self, fresh_stack):
        """Тест чередующихся операций push/pop"""
        fresh_stack.push(100)
        assert fresh_stack.peek() == 100

        fresh_stack.push(200)
        assert fresh_stack.pop() == 200
        assert fresh_stack.peek() == 100

        fresh_stack.push(300)
        fresh_stack.push(400)
        assert fresh_stack.pop() == 400
        assert fresh_stack.pop() == 300
        assert fresh_stack.pop() == 100

        assert fresh_stack.is_empty() == True

    def test_stack_error_conditions(self, fresh_stack):
        """Тест обработки ошибок стека"""
        with pytest.raises(IndexError):
            fresh_stack.pop()

        with pytest.raises(IndexError):
            fresh_stack.peek()

        fresh_stack.push("test")
        fresh_stack.pop()

        with pytest.raises(IndexError):
            fresh_stack.pop()

    def test_stack_size_tracking(self, fresh_stack):
        """Тест отслеживания размера стека"""
        assert len(fresh_stack) == 0

        for i in range(10):
            fresh_stack.push(i)
            assert len(fresh_stack) == i + 1

        for i in range(9, -1, -1):
            fresh_stack.pop()
            assert len(fresh_stack) == i


if __name__ == "__main__":
    pytest.main([__file__, "-v"])