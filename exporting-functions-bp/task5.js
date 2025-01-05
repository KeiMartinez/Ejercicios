export function rubricPassFail(score) {
    if (score < 5) {
        return 'Fail';
    } else {
        return 'Pass';
    }
}