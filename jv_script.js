document.getElementById('trackBtn').addEventListener('click', async () => {
    const name = document.getElementById('userName').value;
    const birth = document.getElementById('birthDate').value;
    const resultDiv = document.getElementById('result');
    const loading = document.getElementById('loading');

    if (!name || !birth) {
        alert("이름과 생년월일을 모두 입력해주세요!");
        return;
    }

    loading.classList.remove('hidden');
    resultDiv.classList.add('hidden');

    try {
        const response = await fetch('/api/tracker', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, birth })
        });

        const data = await response.json();
        
        if (response.ok) {
            resultDiv.innerHTML = `<strong>추적 결과:</strong><br>${data.message}`;
        } else {
            resultDiv.innerText = "추적 실패: " + data.error;
        }
    } catch (e) {
        resultDiv.innerText = "서버 연결 오류가 발생했습니다.";
    } finally {
        loading.classList.add('hidden');
        resultDiv.classList.remove('hidden');
    }
});