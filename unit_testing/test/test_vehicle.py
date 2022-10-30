import pytest
from unit_testing import VehicleInfo


@pytest.mark.unit
class TestClass:

    @pytest.fixture
    def test_setup(self):
        return {
            'electric': VehicleInfo("GLE", True, 50000),
            'non_electric': VehicleInfo("BMW", False, 35000)
        }

    def test_compute_tax_electric_car(self, test_setup):
        vehicle = test_setup['electric']
        assert vehicle.compute_tax() == 1000

    def test_compute_tax_non_electric_car(self, test_setup):
        vehicle = test_setup['non_electric']
        assert vehicle.compute_tax() == 1750

    def test_tax_exception_failure(self, test_setup):
        vehicle = test_setup['non_electric']
        pytest.raises(ValueError, vehicle.compute_tax, -1)

    def test_can_lease(self, test_setup):
        vehicle = test_setup['non_electric']
        assert vehicle.can_lease(60000), True

    def test_cannot_lease(self, test_setup):
        vehicle = test_setup['non_electric']
        assert vehicle.can_lease(30000), False

    def test_negative_income(self, test_setup):
        vehicle = test_setup['non_electric']
        pytest.raises(ValueError, vehicle.can_lease, -2)
