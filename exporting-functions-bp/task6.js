export function rubricExcellent(score) {
    if (score >= 9) {
        return 'Excellent';
    } else {
        return 'Pass';
    }
}