document.addEventListener('DOMContentLoaded', () => {
    // Initialize Charts
    let nutritionChart, workoutChart, progressChart;

    // Nutrition Chart
    const nutritionCtx = document.getElementById('nutritionChart').getContext('2d');
    nutritionChart = new Chart(nutritionCtx, {
        type: 'pie',
        data: {
            labels: ['Protein', 'Carbs', 'Fats'],
            datasets: [{
                data: [0, 0, 0], // Initial empty data
                backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc']
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

    // Workout Chart
    const workoutCtx = document.getElementById('workoutChart').getContext('2d');
    workoutChart = new Chart(workoutCtx, {
        type: 'bar',
        data: {
            labels: [], // Days of the week
            datasets: [{
                label: 'Training Intensity (%)',
                data: [],
                backgroundColor: '#4e73df',
                borderColor: '#375ab5',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true, max: 100 }
            }
        }
    });

    // Progress Chart
    const progressCtx = document.getElementById('progressChart').getContext('2d');
    progressChart = new Chart(progressCtx, {
        type: 'line',
        data: {
            labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
            datasets: [{
                label: 'Fat Reduction (%)',
                data: [22, 21, 20, 19],
                borderColor: '#4e73df',
                tension: 0.4
            }, {
                label: 'Muscle Gain (kg)',
                data: [0.5, 1.0, 1.5, 2.0],
                borderColor: '#1cc88a',
                tension: 0.4
            }, {
                label: 'Calories Burned (kCal)',
                data: [1200, 1300, 1400, 1500],
                borderColor: '#36b9cc',
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: false }
            }
        }
    });

    // Performance Metrics
    const performanceMetrics = [
        { metric: "Fat Reduction", value: "-3%", icon: "fas fa-weight" },
        { metric: "Muscle Gain", value: "+2 kg", icon: "fas fa-dumbbell" },
        { metric: "Calories Burned", value: "1500 kCal", icon: "fas fa-fire" }
    ];

    // Display Metrics
    const metricsList = document.getElementById('performanceMetrics');
    metricsList.innerHTML = performanceMetrics.map(item => `
        <li class="list-group-item d-flex justify-content-between align-items-center">
            <div>
                <i class="${item.icon} me-2"></i>
                ${item.metric}
            </div>
            <span class="badge bg-success">${item.value}</span>
        </li>
    `).join('');

    // Add event listeners to training level buttons
    const levelButtons = document.querySelectorAll('.btn-group .btn');
    levelButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            levelButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to the clicked button
            this.classList.add('active');
        });
    });

    // Workout Form Submission
    document.getElementById('workoutForm').addEventListener('submit', function(e) {
        e.preventDefault();
        const goal = document.getElementById('goal').value;
        const level = document.querySelector('.btn-group .btn.active').dataset.level; // Get active button's level
        const equipment = document.getElementById('equipment').value;

        const plan = generateWorkoutPlan(goal, level, equipment);
        updateWorkoutChart(plan);
        displayExercises(plan);
    });

    // Nutrition Form Submission
    document.getElementById('dietForm').addEventListener('submit', function(e) {
        e.preventDefault();
        const calories = parseInt(document.getElementById('calories').value);
        const dietType = document.getElementById('dietType').value;

        const plan = generateDietPlan(calories, dietType);
        updateNutritionChart(plan);
        displayMeals(plan);
    });

    // Workout Plan Generator
    function generateWorkoutPlan(goal, level, equipment) {
        const plans = {
            'muscle-gain': {
                beginner: {
                    days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                    intensity: [60, 65, 70, 65, 75, 50, 0], // Sunday is rest day
                    exercises: {
                        Monday: [
                            { name: 'Bench Press', sets: '4x8' },
                            { name: 'Lat Pulldown', sets: '3x10' },
                            { name: 'Bodyweight Squats', sets: '4x15' }
                        ],
                        Tuesday: [
                            { name: 'Deadlifts', sets: '4x8' },
                            { name: 'Overhead Press', sets: '4x10' },
                            { name: 'Pull-Ups', sets: '3x8' }
                        ],
                        Wednesday: [
                            { name: 'Incline Bench Press', sets: '4x8' },
                            { name: 'Barbell Rows', sets: '3x10' },
                            { name: 'Lunges', sets: '4x12' }
                        ],
                        Thursday: [
                            { name: 'Deadlifts', sets: '4x8' },
                            { name: 'Overhead Press', sets: '4x10' },
                            { name: 'Pull-Ups', sets: '3x8' }
                        ],
                        Friday: [
                            { name: 'Bench Press', sets: '4x8' },
                            { name: 'Lat Pulldown', sets: '3x10' },
                            { name: 'Bodyweight Squats', sets: '4x15' }
                        ],
                        Saturday: [
                            { name: 'Cardio (Running/Cycling)', sets: '30 mins' }
                        ],
                        Sunday: [
                            { name: 'Rest Day', sets: '-' }
                        ]
                    }
                },
                intermediate: {
                    days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                    intensity: [70, 75, 80, 75, 85, 60, 0], // Sunday is rest day
                    exercises: {
                        Monday: [
                            { name: 'Bench Press', sets: '5x8' },
                            { name: 'Lat Pulldown', sets: '4x10' },
                            { name: 'Barbell Squats', sets: '5x8' }
                        ],
                        Tuesday: [
                            { name: 'Deadlifts', sets: '5x8' },
                            { name: 'Overhead Press', sets: '5x10' },
                            { name: 'Pull-Ups', sets: '4x8' }
                        ],
                        Wednesday: [
                            { name: 'Incline Bench Press', sets: '5x8' },
                            { name: 'Barbell Rows', sets: '4x10' },
                            { name: 'Lunges', sets: '5x12' }
                        ],
                        Thursday: [
                            { name: 'Deadlifts', sets: '5x8' },
                            { name: 'Overhead Press', sets: '5x10' },
                            { name: 'Pull-Ups', sets: '4x8' }
                        ],
                        Friday: [
                            { name: 'Bench Press', sets: '5x8' },
                            { name: 'Lat Pulldown', sets: '4x10' },
                            { name: 'Barbell Squats', sets: '5x8' }
                        ],
                        Saturday: [
                            { name: 'Cardio (Running/Cycling)', sets: '45 mins' }
                        ],
                        Sunday: [
                            { name: 'Rest Day', sets: '-' }
                        ]
                    }
                },
                advanced: {
                    days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                    intensity: [80, 85, 90, 85, 95, 70, 0], // Sunday is rest day
                    exercises: {
                        Monday: [
                            { name: 'Bench Press', sets: '6x8' },
                            { name: 'Lat Pulldown', sets: '5x10' },
                            { name: 'Barbell Squats', sets: '6x8' }
                        ],
                        Tuesday: [
                            { name: 'Deadlifts', sets: '6x8' },
                            { name: 'Overhead Press', sets: '6x10' },
                            { name: 'Pull-Ups', sets: '5x8' }
                        ],
                        Wednesday: [
                            { name: 'Incline Bench Press', sets: '6x8' },
                            { name: 'Barbell Rows', sets: '5x10' },
                            { name: 'Lunges', sets: '6x12' }
                        ],
                        Thursday: [
                            { name: 'Deadlifts', sets: '6x8' },
                            { name: 'Overhead Press', sets: '6x10' },
                            { name: 'Pull-Ups', sets: '5x8' }
                        ],
                        Friday: [
                            { name: 'Bench Press', sets: '6x8' },
                            { name: 'Lat Pulldown', sets: '5x10' },
                            { name: 'Barbell Squats', sets: '6x8' }
                        ],
                        Saturday: [
                            { name: 'Cardio (Running/Cycling)', sets: '60 mins' }
                        ],
                        Sunday: [
                            { name: 'Rest Day', sets: '-' }
                        ]
                    }
                }
            },
            'weight-loss': {
                beginner: {
                    days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                    intensity: [75, 80, 85, 80, 90, 60, 0], // Sunday is rest day
                    exercises: {
                        Monday: [
                            { name: 'Burpees', sets: '3x15' },
                            { name: 'Jumping Jacks', sets: '4x30s' },
                            { name: 'Mountain Climbers', sets: '3x20' }
                        ],
                        Tuesday: [
                            { name: 'Sprints', sets: '10x30s' },
                            { name: 'Push-Ups', sets: '4x15' },
                            { name: 'Plank', sets: '3x1min' }
                        ],
                        Wednesday: [
                            { name: 'Burpees', sets: '3x15' },
                            { name: 'Jumping Jacks', sets: '4x30s' },
                            { name: 'Mountain Climbers', sets: '3x20' }
                        ],
                        Thursday: [
                            { name: 'Sprints', sets: '10x30s' },
                            { name: 'Push-Ups', sets: '4x15' },
                            { name: 'Plank', sets: '3x1min' }
                        ],
                        Friday: [
                            { name: 'Burpees', sets: '3x15' },
                            { name: 'Jumping Jacks', sets: '4x30s' },
                            { name: 'Mountain Climbers', sets: '3x20' }
                        ],
                        Saturday: [
                            { name: 'Cardio (Running/Cycling)', sets: '45 mins' }
                        ],
                        Sunday: [
                            { name: 'Rest Day', sets: '-' }
                        ]
                    }
                },
                intermediate: {
                    days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                    intensity: [80, 85, 90, 85, 95, 70, 0], // Sunday is rest day
                    exercises: {
                        Monday: [
                            { name: 'Burpees', sets: '4x15' },
                            { name: 'Jumping Jacks', sets: '5x30s' },
                            { name: 'Mountain Climbers', sets: '4x20' }
                        ],
                        Tuesday: [
                            { name: 'Sprints', sets: '12x30s' },
                            { name: 'Push-Ups', sets: '5x15' },
                            { name: 'Plank', sets: '4x1min' }
                        ],
                        Wednesday: [
                            { name: 'Burpees', sets: '4x15' },
                            { name: 'Jumping Jacks', sets: '5x30s' },
                            { name: 'Mountain Climbers', sets: '4x20' }
                        ],
                        Thursday: [
                            { name: 'Sprints', sets: '12x30s' },
                            { name: 'Push-Ups', sets: '5x15' },
                            { name: 'Plank', sets: '4x1min' }
                        ],
                        Friday: [
                            { name: 'Burpees', sets: '4x15' },
                            { name: 'Jumping Jacks', sets: '5x30s' },
                            { name: 'Mountain Climbers', sets: '4x20' }
                        ],
                        Saturday: [
                            { name: 'Cardio (Running/Cycling)', sets: '60 mins' }
                        ],
                        Sunday: [
                            { name: 'Rest Day', sets: '-' }
                        ]
                    }
                },
                advanced: {
                    days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                    intensity: [85, 90, 95, 90, 100, 80, 0], // Sunday is rest day
                    exercises: {
                        Monday: [
                            { name: 'Burpees', sets: '5x15' },
                            { name: 'Jumping Jacks', sets: '6x30s' },
                            { name: 'Mountain Climbers', sets: '5x20' }
                        ],
                        Tuesday: [
                            { name: 'Sprints', sets: '15x30s' },
                            { name: 'Push-Ups', sets: '6x15' },
                            { name: 'Plank', sets: '5x1min' }
                        ],
                        Wednesday: [
                            { name: 'Burpees', sets: '5x15' },
                            { name: 'Jumping Jacks', sets: '6x30s' },
                            { name: 'Mountain Climbers', sets: '5x20' }
                        ],
                        Thursday: [
                            { name: 'Sprints', sets: '15x30s' },
                            { name: 'Push-Ups', sets: '6x15' },
                            { name: 'Plank', sets: '5x1min' }
                        ],
                        Friday: [
                            { name: 'Burpees', sets: '5x15' },
                            { name: 'Jumping Jacks', sets: '6x30s' },
                            { name: 'Mountain Climbers', sets: '5x20' }
                        ],
                        Saturday: [
                            { name: 'Cardio (Running/Cycling)', sets: '75 mins' }
                        ],
                        Sunday: [
                            { name: 'Rest Day', sets: '-' }
                        ]
                    }
                }
            }
        };

        return plans[goal][level] || {
            days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            intensity: [50, 55, 60, 55, 65, 40, 0],
            exercises: {
                Monday: [{ name: 'Generic Exercise', sets: '3x10' }],
                Tuesday: [{ name: 'Generic Exercise', sets: '3x10' }],
                Wednesday: [{ name: 'Generic Exercise', sets: '3x10' }],
                Thursday: [{ name: 'Generic Exercise', sets: '3x10' }],
                Friday: [{ name: 'Generic Exercise', sets: '3x10' }],
                Saturday: [{ name: 'Cardio', sets: '30 mins' }],
                Sunday: [{ name: 'Rest Day', sets: '-' }]
            }
        };
    }

    // Nutrition Plan Generator
    function generateDietPlan(calories, dietType) {
        const ratios = {
            balanced: { protein: 30, carbs: 40, fats: 30 },
            keto: { protein: 20, carbs: 10, fats: 70 },
            vegan: { protein: 25, carbs: 50, fats: 25 },
            'low-carb': { protein: 35, carbs: 20, fats: 45 }
        };

        const macros = ratios[dietType];
        const meals = {
            balanced: [
                { time: 'Breakfast', items: ['Oatmeal', 'Eggs', 'Greek Yogurt'] },
                { time: 'Lunch', items: ['Grilled Chicken', 'Quinoa', 'Broccoli'] },
                { time: 'Dinner', items: ['Salmon', 'Sweet Potato', 'Asparagus'] }
            ],
            keto: [
                { time: 'Breakfast', items: ['Avocado', 'Eggs', 'Bacon'] },
                { time: 'Lunch', items: ['Grilled Steak', 'Spinach', 'Cheese'] },
                { time: 'Dinner', items: ['Salmon', 'Zucchini Noodles', 'Butter'] }
            ],
            vegan: [
                { time: 'Breakfast', items: ['Smoothie', 'Banana', 'Almond Butter'] },
                { time: 'Lunch', items: ['Chickpea Salad', 'Quinoa', 'Kale'] },
                { time: 'Dinner', items: ['Lentil Curry', 'Brown Rice', 'Broccoli'] }
            ],
            'low-carb': [
                { time: 'Breakfast', items: ['Scrambled Eggs', 'Spinach', 'Cheese'] },
                { time: 'Lunch', items: ['Grilled Chicken', 'Cauliflower Rice', 'Avocado'] },
                { time: 'Dinner', items: ['Grilled Fish', 'Zucchini', 'Olive Oil'] }
            ]
        };

        return { macros, meals: meals[dietType] };
    }

    // Update Nutrition Chart
    function updateNutritionChart(plan) {
        nutritionChart.data.datasets[0].data = [plan.macros.protein, plan.macros.carbs, plan.macros.fats];
        nutritionChart.update();
    }

    // Display Meals
    function displayMeals(plan) {
        document.getElementById('mealPlan').innerHTML = plan.meals.map(meal => `
            <div class="meal-item mb-3">
                <h6>${meal.time}</h6>
                <p>${meal.items.join(', ')}</p>
            </div>
        `).join('');
    }

    // Update Workout Chart
    function updateWorkoutChart(plan) {
        workoutChart.data.labels = plan.days;
        workoutChart.data.datasets[0].data = plan.intensity;
        workoutChart.update();
    }

    // Display Exercises
    function displayExercises(plan) {
        const today = new Date().toLocaleString('en-US', { weekday: 'long' });
        document.getElementById('exerciseList').innerHTML = plan.days.map(day => `
            <div class="day-plan mb-4">
                <h6>${day} ${day === today ? '(Today)' : ''}</h6>
                <ul class="list-group">
                    ${plan.exercises[day]?.map(ex => `
                        <li class="list-group-item d-flex justify-content-between align-items-center">
                            ${ex.name}
                            <span class="badge bg-primary">${ex.sets}</span>
                        </li>
                    `).join('')}
                </ul>
            </div>
        `).join('');
    }
});