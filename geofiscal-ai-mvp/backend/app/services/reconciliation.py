def reconcile_amounts(budget: float, actual: float, tolerance_pct: float = 5.0):
    variance = actual - budget
    variance_pct = (variance / budget) * 100 if budget else 0
    abs_pct = abs(variance_pct)

    if abs_pct <= tolerance_pct:
        status = 'matched'
        confidence = 0.97
        risk = 0.08
    elif abs_pct <= tolerance_pct * 2:
        status = 'partially_matched'
        confidence = 0.78
        risk = 0.32
    elif variance_pct > tolerance_pct * 4:
        status = 'suspicious'
        confidence = 0.63
        risk = 0.91
    else:
        status = 'unmatched'
        confidence = 0.55
        risk = 0.68

    explanation = (
        f'Budget vs actual variance is {variance_pct:.2f}%. '
        f'Tolerance is ±{tolerance_pct:.2f}%. Classified as {status}.'
    )

    return {
        'status': status,
        'variance': round(variance, 2),
        'variance_pct': round(variance_pct, 2),
        'confidence_score': confidence,
        'risk_score': risk,
        'explanation': explanation,
    }
