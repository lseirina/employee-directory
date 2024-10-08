"""Views for employee-heirarchy."""
from django.shortcuts import render
from core.models import Employee


def employee_heirarchy(request):
    top_managers = Employee.objects.filter(
        manager__isnull=True
        ).prefetch_related('subordinates')

    def get_subordinates(employee):
        """Recursive function to get all subordinates."""
        subordinates = employee.subordinates.all()

        for emp in subordinates:
            return [
                {
                    'employee': emp,
                    'subordinates': get_subordinates(emp)
                }
            ]

    employees_hierarchy = []
    for manager in top_managers:
        employees_hierarchy.append(
           {
               'employee': manager,
               'subordinates': get_subordinates(manager)
            }
        )

    return render(request, 'employee_hierarchy.html', {
        'employees_hierarchy': employees_hierarchy
    })
